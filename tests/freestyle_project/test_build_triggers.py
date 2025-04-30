from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.freestyle_project.freestyle_data import Freestyle


def test_user_can_trigger_builds_remotely(auth_token, freestyle_configs, config):
    wait10 = WebDriverWait(freestyle_configs, 10)
    wait30 = WebDriverWait(freestyle_configs, 30)

    token = auth_token
    trigger_job_api = f"{config.jenkins.base_url}/job/{Freestyle.project_name.replace(" ", "%20")}/build?token={token}"

    trigger_builds_remotely_checkbox = freestyle_configs.find_element(
        By.CSS_SELECTOR,
        "input[name='pseudoRemoteTrigger']~label"
    )
    freestyle_configs.execute_script(
        'arguments[0].scrollIntoView({block: "center", inline: "center"})',
        trigger_builds_remotely_checkbox
    )
    wait10.until(EC.element_to_be_clickable(trigger_builds_remotely_checkbox)).click()
    wait10.until(EC.visibility_of_element_located((By.NAME, "authToken"))).send_keys(token)
    freestyle_configs.find_element(By.NAME, "Submit").click()

    window_before = freestyle_configs.window_handles[0]
    freestyle_configs.switch_to.new_window()
    freestyle_configs.get(trigger_job_api)
    freestyle_configs.switch_to.window(window_before)

    wait10.until(EC.visibility_of_element_located((By.LINK_TEXT, "Dashboard"))).click()
    wait30.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#buildQueue>.pane-content tbody>tr>td"),
        "No builds in the queue.")
    )
    freestyle_configs.find_element(By.LINK_TEXT, "Build History").click()

    builds_list = wait10.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#projectStatus>tbody>tr")))

    assert len(builds_list) == 1, f"Unexpected numbers of builds created {len(builds_list)}"
    assert freestyle_configs.find_element(By.LINK_TEXT, f"{Freestyle.project_name}").is_displayed(), \
        f"No builds created for {Freestyle.project_name}"
    assert freestyle_configs.find_element(By.LINK_TEXT, "#1"), "Unexpected builds enumeration."
