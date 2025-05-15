import re
import json
import logging
import requests

logger = logging.getLogger(__name__)


def get_crumb(response):
    return re.findall(r'data-crumb-value="([a-z0-9]{64})"', response.text)[0]


def get_session(driver):
    session = requests.Session()
    cookies = driver.get_cookies()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    return session


def update_crumb(driver, config):
    session = get_session(driver)
    response = session.get(config.jenkins.base_url + "/crumbIssuer/api/json")
    if response.ok:
        crumb = response.json().get("crumb", "")
        logger.debug(f"update_crumb: {crumb}")
        config.jenkins.update_crumb(crumb)
        return crumb
    else:
        logger.error(f"failed to update crumb, {response.status_code} {response.text}")


def remote_build_trigger(driver, job_name, token, config):
    update_crumb(driver, config)
    session = get_session(driver)
    cred_url = config.jenkins.get_url_with_credentials()
    url = f"{cred_url}/job/{job_name}/build?token={token}&Jenkins-Crumb={config.jenkins.crumb}"
    session.get(url)


def get_substrings(response, from_string, to_string):
    # В Java коде длину ограничивали в 255 символов, я пока не делал. Если возникнут проблемы тогда будем смотреть.
    return set(re.findall(rf'{from_string}(.+?){to_string}', response.text))


def get_page(session, url, config):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = session.get(url, headers=headers)
    if not response.ok:
        logger.debug("failed to get page on the first try, retrying after login")
        session.get(f"{config.jenkins.base_url}/login?from=%2F", headers=headers)
        session.post(config.jenkins.login_url, headers=headers, data=config.jenkins.login_data)
        response = session.get(url, headers=headers)
    if not response.ok:
        raise RuntimeError("could not login")
    return response


def delete_by_link(session, url, names, crumb):
    for name in names:
        response = session.post(
            url=url.format(name),
            headers={"Jenkins-Crumb": crumb, "Content-Type": "application/x-www-form-urlencoded"}
        )
        if not response.ok:
            logger.error(f"delete_by_link, {url=} {response.status_code=} {name=}")


def reset_theme_description(session, config):
    crumb = get_crumb(get_page(session, config.jenkins.base_url, config))

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    desc_json = {"description": "", "Submit": "Submit", "Jenkins-Crumb": crumb}
    desc_payload = f"description=&Jenkins-Crumb={crumb}&json={json.dumps(desc_json)}&Submit=Submit&core:apply=true"
    theme_json = {"userProperty0":{"theme":{
                                              "value":"0",
                                              "stapler-class":"io.jenkins.plugins.thememanager.none.NoOpThemeManagerFactory",
                                              "$class":"io.jenkins.plugins.thememanager.none.NoOpThemeManagerFactory"
                                          }}}
    theme_payload = f"Jenkins-Crumb={crumb}&json={json.dumps(theme_json)}&Submit=Submit&core:apply=true"

    if not session.post(
            url=f"{config.jenkins.base_url}/submitDescription",
            headers=headers,
            data=desc_payload
    ).ok:
        logger.error(f"Description cleanup failed: {desc_payload}")

    if not session.post(
            url=f"{config.jenkins.base_url}/me/my-views/view/all/submitDescription",
            headers=headers,
            data=desc_payload
    ).ok:
        logger.error(f"View description cleanup failed: {desc_payload}")

    if not session.post(
            url=f"{config.jenkins.base_url}/user/{config.jenkins.USERNAME}/appearance/configSubmit",
            headers=headers,
            data=theme_payload
    ).ok:
        logger.error(f"Theme cleanup failed: {theme_payload}")


def delete_jobs_views(session, config):
    main_page = get_page(session, config.jenkins.base_url, config)
    view_page = get_page(session, config.jenkins.base_url + "/me/my-views/view/all/", config)
    crumb = get_crumb(main_page)

    url = config.jenkins.base_url + f"/user/{config.jenkins.USERNAME}" + "/my-views/view/{}/doDelete"
    names = get_substrings(view_page, f'href="/user/{config.jenkins.USERNAME}/my-views/view/', '(?:/"|" class)') - {'all/newJob', 'all/builds'}
    delete_by_link(session, url, names, crumb)

    url = config.jenkins.base_url + "/view/{}/doDelete"
    names = get_substrings(main_page, 'href="view/', '/"')
    delete_by_link(session, url, names, crumb)

    url = config.jenkins.base_url + "/job/{}/doDelete"
    names = get_substrings(main_page, 'href="job/', '/(?:"|build|last)')
    delete_by_link(session, url, names, crumb)


def delete_users(session, config):
    user_page = get_page(session, config.jenkins.base_url + "/manage/securityRealm/", config)
    url = config.jenkins.base_url + "/manage/securityRealm/user/{}/doDelete"
    names = get_substrings(user_page, 'href="user/', '/"') - {config.jenkins.USERNAME}
    crumb = get_crumb(user_page)
    delete_by_link(session, url, names, crumb)


def delete_nodes(session, config):
    node_page = get_page(session, config.jenkins.base_url + "/computer/", config)
    url = config.jenkins.base_url + "/manage/computer/{}/doDelete"
    names = get_substrings(node_page, 'href="../computer/', '/" ') - {"(built-in)"}
    crumb = get_crumb(node_page)
    delete_by_link(session, url, names, crumb)


def delete_domains(session, config):
    system_page = get_page(session, config.jenkins.base_url + "/manage/credentials/store/system/", config)
    url = config.jenkins.base_url + "/manage/credentials/store/system/domain/{}/doDelete"
    names = get_substrings(system_page, 'href="domain/', '/" class')
    crumb = get_crumb(system_page)
    delete_by_link(session, url, names, crumb)


def delete_tokens(session, config):
    security_page = get_page(session, config.jenkins.base_url + f"/user/{config.jenkins.USERNAME}/security/", config)
    url = config.jenkins.base_url + f"/user/{config.jenkins.USERNAME}/descriptorByName/jenkins.security.ApiTokenProperty/revoke"
    uuids = get_substrings(security_page, 'class="token-uuid-input" value="', '">')
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Jenkins-Crumb": get_crumb(security_page)}
    for uuid in uuids:
        logger.info(f"deleting token with uuid {uuid}")
        response = session.post(url=url, headers=headers, data=f"tokenUuid={uuid}")
        if not response.ok:
            logger.error(f"failed to delete token with uuid={uuid}, response code: {response.status_code}")


def clear_data(config):
    session = requests.Session()
    logger.info("running cleanup")
    delete_jobs_views(session, config)
    delete_users(session, config)
    delete_nodes(session, config)
    delete_domains(session, config)
    reset_theme_description(session, config)
    delete_tokens(session, config)


