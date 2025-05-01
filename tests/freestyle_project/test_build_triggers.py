import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.freestyle_project.freestyle_data import Freestyle

logger = logging.getLogger(__name__)


def test_user_can_trigger_builds_remotely(revoke_project_tokens, auth_token, freestyle, config):
    wait10 = WebDriverWait(freestyle, 10)
    wait60 = WebDriverWait(freestyle, 60)

    token = auth_token

    checkbox = freestyle.find_element(By.CSS_SELECTOR, "input[name='pseudoRemoteTrigger']~label")
    freestyle.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', checkbox)
    wait10.until(EC.element_to_be_clickable(checkbox)).click()
    wait10.until(EC.visibility_of_element_located((By.NAME, "authToken"))).send_keys(token)
    freestyle.find_element(By.NAME, "Submit").click()

    app_window = freestyle.window_handles[0]

    freestyle.switch_to.new_window()
    freestyle.get("http://localhost:8080/crumbIssuer/api/json")

    crumb = freestyle.find_element(By.CSS_SELECTOR, "body").text.split('"')[7]
    job_name = Freestyle.encoded_project_name
    username = config.jenkins.USERNAME
    password = config.jenkins.PASSWORD
    server = f"{config.jenkins.HOST}:{config.jenkins.PORT}"
    base_url = config.jenkins.base_url

    api_urls = {
        "api_1": f"{base_url}/job/{job_name}/build?token={token}",
        "api_2": f"{base_url}/job/{job_name}/build?token={token}&Jenkins-Crumb={crumb}",
        "api_3": f"http://{username}:{password}@{server}/job/{job_name}/build?token={token}&Jenkins-Crumb={crumb}"
    }

    freestyle.switch_to.new_window()
    freestyle.get(api_urls["api_1"])
    # freestyle.refresh()
    logger.info(f"Triggered build at: {freestyle.current_url}")
    logger.info(f"Build response: {freestyle.find_element(By.CSS_SELECTOR, 'body').text}")

    freestyle.switch_to.window(app_window)

    wait10.until(EC.visibility_of_element_located((By.LINK_TEXT, "Dashboard"))).click()
    logger.info(f"Returned to Dashboard: {freestyle.current_url}")

    wait10.until(EC.visibility_of_element_located((By.LINK_TEXT, "Build History"))).click()
    logger.info(f"Viewing Build History: {freestyle.current_url}")

    queue_status = (By.CSS_SELECTOR, "#buildQueue .pane-content")
    wait60.until(EC.text_to_be_present_in_element(queue_status, "No builds in the queue."))
    logger.info("Waiting for the build to finish...")

    freestyle.refresh()
    logger.info("Build finished. Refreshing status.")

    builds = wait10.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#projectStatus>tbody>tr")))

    assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    assert freestyle.find_element(By.LINK_TEXT, f"{Freestyle.project_name}").is_displayed(), \
        f"No build entry found for project '{Freestyle.project_name}'"
    assert freestyle.find_element(By.LINK_TEXT, "#1"), "Build #1 not found."
