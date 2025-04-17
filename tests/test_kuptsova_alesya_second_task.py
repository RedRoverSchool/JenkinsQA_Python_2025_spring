import pytest
from selenium.webdriver.common.by import By

username_correct = 'problem_user'
password_correct = 'secret_sauce'

@pytest.fixture
def setup_driver(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_log_in_with_unfilled_fields(setup_driver):
    setup_driver.find_element(By.NAME, 'login-button').click()

    error_message = setup_driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.text == 'Epic sadface: Username is required'

def test_user_can_log_out_of_the_site(setup_driver):
    setup_driver.find_element(By.ID, 'user-name').send_keys(username_correct)
    setup_driver.find_element(By.ID, 'password').send_keys(password_correct)
    setup_driver.find_element(By.NAME, 'login-button').click()
    setup_driver.find_element(By.ID, 'react-burger-menu-btn').click()
    setup_driver.find_element(By.ID, 'logout_sidebar_link').click()

    assert setup_driver.current_url == 'https://www.saucedemo.com/', 'wrong url'
