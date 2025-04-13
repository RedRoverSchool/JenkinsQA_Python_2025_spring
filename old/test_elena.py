from selenium import webdriver
from selenium.webdriver.common.by import By

def test_no_username_error_message():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.NAME, 'login-button').click()

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.text == "Epic sadface: Username is required"
    driver.quit()

def test_moving_to_new_url():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    driver.quit()