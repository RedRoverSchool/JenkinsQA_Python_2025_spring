from selenium import webdriver
from selenium.webdriver.common.by import By

def test_required_password():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, 'user-name').send_keys('123')
    driver.find_element(By.ID, 'login-button').click()
    error_message = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    assert error_message.text == 'Epic sadface: Password is required'
    driver.quit()