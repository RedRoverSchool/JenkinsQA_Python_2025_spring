import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_standard_user_log_in(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert driver.title == "Swag Labs", "wrong title"
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "wrong URL"


def test_locked_out_user_log_in(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."


def test_wrong_password_log_in(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("***")
    driver.find_element(By.ID, "login-button").click()

    password_error_message = driver.find_element(
        By.XPATH, "//h3[@data-test='error']"
    ).text
    assert (
        password_error_message
        == "Epic sadface: Username and password do not match any user in this service"
    )
