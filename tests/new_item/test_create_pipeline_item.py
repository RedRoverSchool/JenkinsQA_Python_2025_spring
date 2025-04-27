from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_create_pipeline_item_1(main_page):
    wait = WebDriverWait(main_page, 10)
    item_name = "Pipeline one"

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='newJob']"))).click()
    main_page.find_element(By.CLASS_NAME, "jenkins-input").send_keys(item_name)
    main_page.find_element(By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob").click()
    main_page.find_element(By.ID, "ok-button").click()
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    main_page.find_element(By.ID, "jenkins-home-link").click()
    wait.until(EC.visibility_of_element_located((By.ID, "projectstatus")))
    new_item_name = main_page.find_element(By.CLASS_NAME, "inside").text

    assert new_item_name == item_name


