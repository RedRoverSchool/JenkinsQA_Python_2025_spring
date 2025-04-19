import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def login_page(driver):
    def _login(username, password):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        return driver

    return _login


def test_login_successful(login_page):
    driver = login_page("standard_user", "secret_sauce")
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "wrong URL"


def test_wrong_password_error_message(login_page):
    driver = login_page("standard_user", "wrong_pass")
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    )
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service", \
        "error message is not displayed"


def test_locked_out_user_error_message(login_page):
    driver = login_page("locked_out_user", "secret_sauce")
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    )
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out.", \
        "error message is not displayed"


def test_login_with_empty_fields(login_page):
    driver = login_page(username="", password="")
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    )
    assert error_message.text == "Epic sadface: Username is required", \
        "error message is not displayed"
