from selenium import webdriver
from selenium.webdriver.common.by import By

def test_required_username():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, 'login-button').click()
    error_message = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    assert error_message.text == 'Epic sadface: Username is required'
    driver.quit()