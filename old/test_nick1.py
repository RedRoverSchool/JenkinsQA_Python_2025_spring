from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_abc_user():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("abc")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    error_message = driver.find_element(By.XPATH, '//h3[data-test="error"]')
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
    driver.quit()


def test_locked_out_user_error_message():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("locked_out_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    error_message = driver.find_element(By.XPATH, '//h3[data-test="error"]')
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."
    driver.quit()


def test_problem_user_url_check():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("problem_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    assert driver.current_url == "https://www.saucedemo.com/", "wrong url"
    driver.quit()

def test_locked_out_user_url_check():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("locked_out_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    assert driver.current_url == "https://www.saucedemo.com/", "wrong url"
    driver.quit()