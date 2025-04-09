import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    return driver


def test_login_page_opens(login_page):
    header = login_page.find_element(By.XPATH, '//*[@id="login"]/h2')
    assert header.text == "Test login"

def test_login_successful(login_page):
    login_page.find_element(By.ID, "username").send_keys("student")
    login_page.find_element(By.ID, "password").send_keys("Password123")
    login_page.find_element(By.XPATH, '//button[@id="submit"]').click()
    time.sleep(1)
    assert "practicetestautomation.com/logged-in-successfully/" in login_page.current_url

def test_login_with_invalid_password(login_page):
    login_page.find_element(By.ID, "username").send_keys("student")
    login_page.find_element(By.ID, "password").send_keys("incorrectPassword")
    login_page.find_element(By.XPATH, '//button[@id="submit"]').click()
    time.sleep(1)
    error_message = login_page.find_element(By.XPATH, '//div[@id="error"]')
    assert error_message.text == "Your password is invalid!"

def test_login_with_invalid_username(login_page):
    login_page.find_element(By.ID, "username").send_keys("incorrectUser")
    login_page.find_element(By.ID, "password").send_keys("Password123")
    login_page.find_element(By.XPATH, '//button[@id="submit"]').click()
    time.sleep(1)
    error_message = login_page.find_element(By.XPATH, '//div[@id="error"]')
    assert error_message.text == "Your username is invalid!"
