from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.saucedemo.com/'
user_name_standard = 'standard_user'git
password = 'secret_sauce'

def test_standard_user_login_url_check():
    driver = webdriver.Chrome()

    driver.get(url)
    driver.find_element(By.ID, 'user-name').send_keys(user_name_standard)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()

    assert 'inventory' in driver.current_url
    driver.quit()

def test_standard_user_login_header_check():
    driver = webdriver.Chrome()

    driver.get(url)
    driver.find_element(By.ID, 'user-name').send_keys(user_name_standard)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()

    assert driver.find_element(By.CSS_SELECTOR, "span[data-test = 'title']").text == 'Products'
    driver.quit()
