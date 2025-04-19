from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def login_to_saucedemo(driver, user_name):
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys(user_name)
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

@pytest.mark.parametrize('user_name', ['standard_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user'])
def test_successful_login_opens_inventory_page(driver, user_name):
    login_to_saucedemo(driver, user_name)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', f'Wrong url when registering {user_name}'
    assert driver.find_element(By.CSS_SELECTOR, "span[data-test = 'title']").text == 'Products'
