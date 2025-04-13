import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver2(driver):
    driver.maximize_window()
    yield driver

@pytest.fixture
def sauce(driver2):
    driver2.get("https://www.saucedemo.com/")
    return driver2

def test_successful_login_redirect(sauce):
    sauce.find_element(By.ID, 'user-name').send_keys("standard_user")
    sauce.find_element(By.ID, 'password').send_keys("secret_sauce")
    sauce.find_element(By.ID, 'login-button').click()

    time.sleep(3)

    assert sauce.current_url == "https://www.saucedemo.com/inventory.html", "Login did not redirect to inventory page"
