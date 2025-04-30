from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def browser(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_success_log_in(browser):
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"


def test_locked_out_user(browser):
    browser.find_element(By.ID, "user-name").send_keys("locked_out_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    assert browser.find_element(By.XPATH,
                                '//*[@data-test="error"]').text == "Epic sadface: Sorry, this user has been locked out."
