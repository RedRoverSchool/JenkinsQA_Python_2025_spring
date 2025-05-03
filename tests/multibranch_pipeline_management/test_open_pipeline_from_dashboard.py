from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


def test_access_multibranch(main_page):
    wait = WebDriverWait(main_page, 10)
    item_name = f"Multibranch_{datetime.now().strftime('%H%M%S')}"

    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New Item"))).click()
    main_page.find_element(By.ID, "name").send_keys(item_name)
    item_type = main_page.find_element(
        By.CLASS_NAME,
        "org_jenkinsci_plugins_workflow_multibranch_WorkflowMultiBranchProject",
    )

    main_page.execute_script("arguments[0].scrollIntoView(true);", item_type)
    time.sleep(0.5)
    item_type.click()
    main_page.find_element(By.ID, "ok-button").click()
    wait.until(EC.presence_of_element_located((By.ID, "general")))
    wait.until(EC.presence_of_element_located((By.ID, "jenkins-home-link")))
    main_page.find_element(By.ID, "jenkins-home-link").click()
    wait.until(EC.presence_of_element_located((By.ID, "projectstatus")))

    actual_item = main_page.find_element(By.CLASS_NAME, "inside").text
    assert actual_item == item_name
