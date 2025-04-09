from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.saucedemo.com/'
username_standard = 'standard_user'
password = 'secret_sauce'

def test_standard_user_login():
    driver = webdriver.Chrome()

    driver.get(url)
    driver.find_element(By.ID, 'user-name').send_keys(username_standard)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()

    assert 'inventory' in driver.current_url
    driver.quit()

def test_standard_user_title():
    driver = webdriver.Chrome()

    driver.get(url)
    driver.find_element(By.ID, 'user-name').send_keys(username_standard)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()

    assert driver.find_element(By.CSS_SELECTOR, "span[data-test = 'title']").text == 'Products'
    driver.quit()
