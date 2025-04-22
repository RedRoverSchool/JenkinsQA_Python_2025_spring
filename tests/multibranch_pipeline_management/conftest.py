import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def login_page(driver, config):
    driver.get(config.jenkins.base_url + "/login?from=%2F")
    return driver


@pytest.fixture(scope="function")
def main_page(login_page, config):
    login_page.find_element(By.ID, "j_username").send_keys(config.jenkins.USERNAME)
    login_page.find_element(By.ID, "j_password").send_keys(config.jenkins.PASSWORD)
    login_page.find_element(By.NAME, "Submit").click()
    wait5 = WebDriverWait(login_page, 5, poll_frequency=0.5)
    wait5.until(EC.url_changes(config.jenkins.base_url + "/login?from=%2F"))
    return login_page
