import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username_correct = 'problem_user'
password_correct = 'secret_sauce'


@pytest.fixture
def saucedemo(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_log_in_with_unfilled_fields(saucedemo):
    saucedemo.find_element(By.NAME, 'login-button').click()

    error_message = saucedemo.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.text == 'Epic sadface: Username is required'


def test_user_can_log_out_of_the_site(saucedemo):
    wait = WebDriverWait(saucedemo, 5)
    saucedemo.find_element(By.ID, 'user-name').send_keys(username_correct)
    saucedemo.find_element(By.ID, 'password').send_keys(password_correct)
    saucedemo.find_element(By.NAME, 'login-button').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn')))
    saucedemo.find_element(By.ID, 'react-burger-menu-btn').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
    saucedemo.find_element(By.ID, 'logout_sidebar_link').click()
    wait.until(EC.visibility_of_element_located((By.NAME, 'login-button')))

    assert saucedemo.current_url == 'https://www.saucedemo.com/', 'wrong url'