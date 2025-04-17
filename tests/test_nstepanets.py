import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def login_page(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    return driver

@pytest.fixture(scope="function")
def wait(driver):
    driver_wait = WebDriverWait(driver, 1)
    return driver_wait


def test_login_page_opens(login_page):
    header = login_page.find_element(By.XPATH, '//*[@id="login"]/h2')
    assert header.text == "Test login"

def test_login_successful(login_page, wait):
    login_page.find_element(By.ID, "username").send_keys("student")
    login_page.find_element(By.ID, "password").send_keys("Password123")
    login_page.find_element(By.XPATH, '//button[@id="submit"]').click()
    wait.until(EC.url_contains("practicetestautomation.com/logged-in-successfully/"), "URL is not as expected")
    message = login_page.find_element(By.XPATH, '//h1')
    assert message.text == "Logged In Successfully"

def test_login_with_invalid_password(login_page, wait):
    login_page.find_element(By.ID, "username").send_keys("student")
    login_page.find_element(By.ID, "password").send_keys("incorrectPassword")
    login_page.find_element(By.XPATH, '//button[@id="submit"]').click()
    error_message = login_page.find_element(By.XPATH, '//div[@id="error"]')
    wait.until(EC.visibility_of(error_message), "Error message not displayed")
    assert error_message.text == "Your password is invalid!"

def test_login_with_invalid_username(login_page, wait):
    login_page.find_element(By.ID, "username").send_keys("incorrectUser")
    login_page.find_element(By.ID, "password").send_keys("Password123")
    login_page.find_element(By.XPATH, '//button[@id="submit"]').click()
    error_message = login_page.find_element(By.XPATH, '//div[@id="error"]')
    wait.until(EC.visibility_of(error_message), "Error message not displayed")
    assert error_message.text == "Your username is invalid!"
