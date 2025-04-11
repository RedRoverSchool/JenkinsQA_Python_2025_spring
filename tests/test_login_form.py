from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_standart_user():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    username_fild = driver.find_element(By.XPATH, "//input[@id='user-name']")
    username_fild.send_keys('standard_user')
    password_fild = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_fild.send_keys('secret_sauce')
    login_bottom = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_bottom.click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    driver.quit()

def test_locked_out_user():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys('locked_out_user')
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//input[@id="login-button"]').click()
    error_message = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
    assert error_message.text == 'Epic sadface: Sorry, this user has been locked out.'
    driver.quit()

