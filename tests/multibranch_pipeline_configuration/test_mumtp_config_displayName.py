from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.freestyle_project.freestyle_data import Freestyle
import time

def test_display_name_exist(main_page):
    wait = WebDriverWait(main_page, 20)
    main_page.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    wait.until(EC.presence_of_element_located((By.ID, 'name'))).send_keys("project-name")
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "org_jenkinsci_plugins_workflow_multibranch_WorkflowMultiBranchProject"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    display_name = wait.until(EC.presence_of_element_located((By.NAME, '_.displayNameOrNull')))
    assert display_name.is_displayed()
