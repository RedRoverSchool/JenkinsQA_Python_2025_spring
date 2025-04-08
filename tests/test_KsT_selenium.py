import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def login(driver, user_name, password):
    driver.find_element(By.ID, "user-name").send_keys(user_name)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def test_successful_login(driver):
    login(driver, "standard_user", "secret_sauce")
    time.sleep(2)
    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    login(driver, "invalid_user", "wrong_password")
    time.sleep(2)
    error = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username and password do not match" in error