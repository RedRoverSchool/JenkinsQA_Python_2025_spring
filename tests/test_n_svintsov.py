import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pytest



@pytest.fixture
def sauce_site(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_locked_out_user_error_message(driver: WebDriver, sauce_site):
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."


def test_locked_out_user_url_check(driver: WebDriver, sauce_site):

        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()

        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error_message.text == "Epic sadface: Sorry, this user has been locked out."




