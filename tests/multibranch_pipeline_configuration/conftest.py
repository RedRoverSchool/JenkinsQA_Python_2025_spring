import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.multibranch_pipeline_configuration.mbp_data import Data


@pytest.fixture()
def mbp_conf_page(driver, main_page):
    driver.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    driver.find_element(By.ID, "name").send_keys(Data.PROJECT_NAME)
    driver.find_element(By.CLASS_NAME, "org_jenkinsci_plugins_workflow_multibranch_WorkflowMultiBranchProject").click()
    driver.find_element(By.ID, "ok-button").click()

    return main_page


@pytest.fixture()
def toggle(mbp_conf_page):
    wait2 = WebDriverWait(mbp_conf_page, 2, poll_frequency=0.5)

    return wait2.until(EC.visibility_of_element_located((By.CLASS_NAME, "jenkins-toggle-switch__label__checked-title")))


@pytest.fixture()
def toggle_tooltip(mbp_conf_page):
    wait2 = WebDriverWait(mbp_conf_page, 2, poll_frequency=0.5)

    return wait2.until(EC.visibility_of_element_located((By.ID, "toggle-switch-enable-disable-project")))


@pytest.fixture()
def span_general(driver, mbp_conf_page):
    return driver.find_element(By.XPATH, "//span[text()='General']")
