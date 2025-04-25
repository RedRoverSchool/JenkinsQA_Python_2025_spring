from selenium.webdriver.common.by import By
from conftest import logger
from tests.multibranch_pipeline_configuration.mbp_data import Data


def test_default_state_of_the_toggle(driver, main_page):
    driver.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    driver.find_element(By.ID, "name").send_keys(Data.PROJECT_NAME)
    driver.find_element(By.CLASS_NAME, "hudson_matrix_MatrixProject").click()
    driver.find_element(By.ID, "ok-button").click()

    assert driver.find_element(
        By.CLASS_NAME, "jenkins-toggle-switch__label__checked-title").text == "Enabled", \
        logger.error("The wrong text of the found element!")
