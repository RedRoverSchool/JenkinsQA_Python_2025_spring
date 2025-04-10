from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_locked_out_user():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."

    driver.quit()



def test_standard_user():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(2)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    driver.quit()



def test_empty_password():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message.text == "Epic sadface: Password is required"

    driver.quit()



def test_empty_username():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message.text == "Epic sadface: Username is required"

    driver.quit()