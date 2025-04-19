import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def sauce(driver):
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    return driver

def test_login_cor_pas(sauce):

    sauce.find_element(By.XPATH,'//input[@name="username"]').send_keys('Admin')
    sauce.find_element(By.NAME,'password').send_keys('admin123')
    sauce.find_element(By.XPATH, '//button[@type="submit"]').click()

    assert sauce.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'


def test_log_with_incor_password(sauce):
    sauce.find_element(By.XPATH,'//input[@name="username"]').send_keys('Admin')
    sauce.find_element(By.NAME,'password').send_keys('admin124')
    sauce.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(3)
    error_message = sauce.find_element(By.XPATH, '//p[text()="Invalid credentials"]')

    assert error_message.text =='Invalid credentials'
