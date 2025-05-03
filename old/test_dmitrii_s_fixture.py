from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def login(driver):
    def _login(username, password="secret_sauce"):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.NAME, "login-button").click()

    return _login


def test_locked_out_user_error_message_css(driver, login):
    login("locked_out_user")
    error_element = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    assert (
        "Epic sadface: Sorry, this user has been locked out." in error_element.text
    ), f"Expected full error message not found. Got: {error_element.text}"


def test_locked_out_user_error_message_xpath(driver, login):
    login("locked_out_user")
    error_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert (
        "Epic sadface: Sorry, this user has been locked out." in error_element.text
    ), f"Expected full error message not found. Got: {error_element.text}"


def test_error_user_price_item(driver, login):
    login("error_user")
    price_element = driver.find_element(
        By.XPATH, "(//*[@data-test='inventory-item-price'])[2]"
    )
    assert price_element.text == "$9.99", f"Unexpected price: {price_element.text}"


def test_error_user_url_check(driver, login):
    login("error_user")
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "wrong url"
