import logging
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.freestyle_project.freestyle_data import Freestyle

logger = logging.getLogger(__name__)


def test_user_can_trigger_builds_remotely(revoke_tokens, auth_token, freestyle, config):
    wait10 = WebDriverWait(freestyle, 10)
    wait60 = WebDriverWait(freestyle, 60)

    token = auth_token

    trigger_builds_remotely_checkbox = freestyle.find_element(By.CSS_SELECTOR,
                                                              "input[name='pseudoRemoteTrigger']~label")
    freestyle.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})',
                             trigger_builds_remotely_checkbox)
    wait10.until(EC.element_to_be_clickable(trigger_builds_remotely_checkbox)).click()
    wait10.until(EC.visibility_of_element_located((By.NAME, "authToken"))).send_keys(token)
    freestyle.find_element(By.NAME, "Submit").click()

    app_window = freestyle.window_handles[0]

    freestyle.switch_to.new_window()
    freestyle.get("http://localhost:8080/crumbIssuer/api/json")

    crumb = freestyle.find_element(By.CSS_SELECTOR, "body").text.split('"')[7]
    job_name = Freestyle.project_name.replace(" ", "%20")
    username = config.jenkins.USERNAME
    password = config.jenkins.PASSWORD
    server = f"{config.jenkins.HOST}:{config.jenkins.PORT}"

    trigger_job_api_1 = f"{config.jenkins.base_url}/job/{job_name}/build?token={token}"
    trigger_job_api_2 = f"{config.jenkins.base_url}/job/{job_name}/build?token={token}&Jenkins-Crumb={crumb}"
    trigger_job_api_3 = f"http://{username}:{password}@{server}/job/{job_name}/build?token={token}&Jenkins-Crumb={crumb}"

    # freestyle.switch_to.new_window()
    # freestyle.get(trigger_job_api_1)
    # logger.info(f"WINDOW 1: {freestyle.current_url}")
    # logger.info(f"WINDOW 1: {freestyle.find_element(By.CSS_SELECTOR, "body").text}")

    # freestyle.switch_to.new_window()
    # freestyle.get(trigger_job_api_2)
    # logger.info(f"WINDOW 2: {freestyle.current_url}")
    # logger.info(f"WINDOW 2: {freestyle.find_element(By.CSS_SELECTOR, "body").text}")

    freestyle.switch_to.new_window()
    freestyle.get(trigger_job_api_3)
    freestyle.refresh()
    logger.info(f"WINDOW 3: {freestyle.current_url}")
    logger.info(f"WINDOW 3: {freestyle.find_element(By.CSS_SELECTOR, "body").text}")

    freestyle.switch_to.window(app_window)

    wait10.until(EC.visibility_of_element_located((By.LINK_TEXT, "Dashboard"))).click()
    logger.info(f"On Dashboard page: {freestyle.current_url}")

    wait10.until(EC.visibility_of_element_located((By.LINK_TEXT, "Build History"))).click()
    logger.info(f"On Build History page: {freestyle.current_url}")

    # wait60.until(EC.text_to_be_present_in_element(
    #     (By.CSS_SELECTOR, "#buildQueue>.pane-content tbody>tr>td"),
    #     "No builds in the queue.")
    # )

    sleep(60)

    freestyle.refresh()

    logger.info(f"After build finished")

    builds_list = wait10.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#projectStatus>tbody>tr")))
    logger.info(f"{len(builds_list)}")

    assert len(builds_list) == 1, f"Unexpected numbers of builds created {len(builds_list)}"
    assert freestyle.find_element(By.LINK_TEXT, f"{Freestyle.project_name}").is_displayed(), \
        f"No builds created for {Freestyle.project_name}"
    assert freestyle.find_element(By.LINK_TEXT, "#1"), "Unexpected builds enumeration."
