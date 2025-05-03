import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.freestyle_project.freestyle_data import Freestyle

logger = logging.getLogger(__name__)


def test_user_can_trigger_builds_remotely(revoke_project_tokens, auth_token, freestyle, config):
    wait10 = WebDriverWait(freestyle, 10)

    token = auth_token

    checkbox = freestyle.find_element(By.CSS_SELECTOR, "input[name='pseudoRemoteTrigger']~label")
    freestyle.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', checkbox)
    wait10.until(EC.element_to_be_clickable(checkbox)).click()
    wait10.until(EC.visibility_of_element_located((By.NAME, "authToken"))).send_keys(token)
    freestyle.find_element(By.NAME, "Submit").click()

    app_window = freestyle.window_handles[0]

    freestyle.switch_to.new_window()
    freestyle.get(f"{config.jenkins.base_url}/crumbIssuer/api/json")

    crumb = freestyle.find_element(By.CSS_SELECTOR, "body").text.split('"')[7]
    job_name = Freestyle.encoded_project_name
    username = config.jenkins.USERNAME
    password = config.jenkins.PASSWORD
    server = f"{config.jenkins.HOST}:{config.jenkins.PORT}"
    api_url = f"http://{username}:{password}@{server}/job/{job_name}/build?token={token}&Jenkins-Crumb={crumb}"

    freestyle.switch_to.new_window()
    freestyle.get(api_url)
    logger.info(f"Triggered build at: {freestyle.current_url}")

    freestyle.switch_to.window(app_window)
    wait10.until(EC.visibility_of_element_located((By.LINK_TEXT, "Dashboard"))).click()
    wait10.until(EC.visibility_of_element_located((By.LINK_TEXT, "Build History"))).click()

    logger.info("Waiting for the build to finish...")
    sleep(10)
    logger.info("Refreshing status.")
    freestyle.refresh()

    builds = wait10.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#projectStatus>tbody>tr")))

    assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    assert freestyle.find_element(By.LINK_TEXT, f"{Freestyle.project_name}").is_displayed(), \
        f"No build entry found for project '{Freestyle.project_name}'"
    assert freestyle.find_element(By.LINK_TEXT, "#1"), "Build #1 not found."
