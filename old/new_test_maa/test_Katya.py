import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def sauce(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_locked_out_user_url_check(sauce):
    sauce.find_element(By.ID, "user-name").send_keys("error_user")
    sauce.find_element(By.ID, "password").send_keys("secret_sauce")
    sauce.find_element(By.NAME, "login-button").click()

    assert sauce.current_url == "https://www.saucedemo.com/inventory.html", "wrong url"
