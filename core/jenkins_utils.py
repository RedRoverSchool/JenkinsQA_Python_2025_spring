import re
import json
import logging

import allure
import requests

logger = logging.getLogger(__name__)


@allure.step("Extract Jenkins crumb token from HTML response.")
def get_crumb(response):
    return re.findall(r'data-crumb-value="([a-z0-9]{64})"', response.text)[0]


@allure.step("Create requests session using Selenium WebDriver cookies.")
def get_session(driver):
    session = requests.Session()
    cookies = driver.get_cookies()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    return session


@allure.step("Fetch and update Jenkins CSRF crumb token.")
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


@allure.step("Trigger Jenkins job build remotely using API token.")
def remote_build_trigger(driver, job_name, token, config):
    update_crumb(driver, config)
    session = get_session(driver)
    cred_url = config.jenkins.get_url_with_credentials()
    url = f"{cred_url}/job/{job_name}/build?token={token}&Jenkins-Crumb={config.jenkins.crumb}"
    session.get(url)


def get_job_info(driver, job_name, config):
    update_crumb(driver, config)
    session = get_session(driver)
    url = f"{config.jenkins.base_url}/job/{job_name}/config.xml"
    try:
        response = session.get(url)
        logger.debug(f"{job_name} config: {response.text}")
    except Exception as e:
        logger.error(f"get_job_info: {str(e)}")

def get_build_info(driver, job_name, config):
    update_crumb(driver, config)
    session = get_session(driver)
    url = f"{config.jenkins.base_url}/job/{job_name}/api/json?tree=builds[number,url]"
    logger.debug(f"Getting information on the {job_name}'s builds")
    try:
        response = session.get(url)
        logger.debug(f"{job_name} builds: {response.text}")
        if not response.ok:
            logger.error("Getting build's info failed")
            return
        response_json = response.json()
        for build in response_json["builds"]:
            url = f"{config.jenkins.base_url}/job/{job_name}/{build["number"]}/api/json?tree=actions[causes[*]]"
            response = session.get(url)
            if not response.ok:
                logger.error("Getting build's info failed")
                return
            descriptions = [cause.get("shortDescription", "failed to get description")
                           for act in response.json().get("actions", [])
                           for cause in act.get("causes", [])]
            logger.info(f"Builds {job_name}/#{build["number"]} cause: {descriptions}")
    except Exception as e:
        logger.error(f"get_build_info: {str(e)}")


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


@allure.step("Reset Jenkins user theme and descriptions to default settings.")
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


@allure.step("Delete all existing jobs and views for the user session.")
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


@allure.step("Delete all Jenkins users except the current user.")
def delete_users(session, config):
    user_page = get_page(session, config.jenkins.base_url + "/manage/securityRealm/", config)
    url = config.jenkins.base_url + "/manage/securityRealm/user/{}/doDelete"
    names = get_substrings(user_page, 'href="user/', '/"') - {config.jenkins.USERNAME}
    crumb = get_crumb(user_page)
    delete_by_link(session, url, names, crumb)


@allure.step("Delete all Jenkins nodes except the built-in node.")
def delete_nodes(session, config):
    node_page = get_page(session, config.jenkins.base_url + "/computer/", config)
    url = config.jenkins.base_url + "/manage/computer/{}/doDelete"
    names = get_substrings(node_page, 'href="../computer/', '/" ') - {"(built-in)"}
    crumb = get_crumb(node_page)
    delete_by_link(session, url, names, crumb)


@allure.step("Delete all credential domains from Jenkins system store.")
def delete_domains(session, config):
    system_page = get_page(session, config.jenkins.base_url + "/manage/credentials/store/system/", config)
    url = config.jenkins.base_url + "/manage/credentials/store/system/domain/{}/doDelete"
    names = get_substrings(system_page, 'href="domain/', '/" class')
    crumb = get_crumb(system_page)
    delete_by_link(session, url, names, crumb)


@allure.step("Revoke all API tokens for the current Jenkins user.")
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


@allure.step("Generate a new Jenkins API token for the current user.")
def generate_token(config, driver, token_name="api-token"):
    update_crumb(driver, config)
    session = get_session(driver)
    security_page = get_page(session, config.jenkins.base_url + f"/user/{config.jenkins.USERNAME}/security/", config)
    url = config.jenkins.base_url + f"/user/{config.jenkins.USERNAME}/descriptorByName/jenkins.security.ApiTokenProperty/generateNewToken"
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Jenkins-Crumb": get_crumb(security_page)}
    data = f"newTokenName={token_name}"

    logger.info(f"Generating Jenkins API token with name: {token_name}")
    response = session.post(url=url, headers=headers, data=data)

    if not response.ok:
        logger.error(f"Failed to generate token. Status: {response.status_code}, Response: {response.text}")
        return None

    try:
        token_value = response.json()["data"]["tokenValue"]
        logger.info(f"Generated token: {token_value[:4]}...")  # Log partial token only
        return token_value
    except Exception as e:
        logger.error(f"Failed to parse token response: {e}")
        return None


@allure.step("Clean up Jenkins data.")
def clear_data(config):
    session = requests.Session()
    logger.info("running cleanup")
    delete_jobs_views(session, config)
    delete_users(session, config)
    delete_nodes(session, config)
    delete_domains(session, config)
    reset_theme_description(session, config)
    delete_tokens(session, config)


