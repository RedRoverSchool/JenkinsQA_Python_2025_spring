import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


URL = "https://www.saucedemo.com/"

def test_login():
    driver = webdriver.Chrome()

    driver.get(URL)
    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()


    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    driver.quit()


def test_locked_out_user():
    driver = webdriver.Chrome()

    driver.get(URL)
    driver.find_element(By.ID, 'user-name').send_keys("locked_out_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."
    driver.quit()


def test_invalid_password():
    driver = webdriver.Chrome()

    driver.get(URL)
    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, 'password').send_keys("secret")
    driver.find_element(By.NAME, 'login-button').click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
    driver.quit()

def test_empty_username_field():
    driver = webdriver.Chrome()

    driver.get(URL)
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Username is required"
    driver.quit()


def test_empty_password_field():
    driver = webdriver.Chrome()

    driver.get(URL)
    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.NAME, 'login-button').click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Password is required"
    driver.quit()


def test_empty_username_password_fields():
    driver = webdriver.Chrome()

    driver.get(URL)
    driver.find_element(By.NAME, 'login-button').click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Username is required"
    driver.quit()

def test_open_sidebar_menu():
    driver = webdriver.Chrome()

    driver.get(URL)
    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()
    driver.find_element(By.XPATH, "//button[text()='Open Menu']").click()

    assert driver.find_element(By.XPATH, "// a[text() = 'About']")
    driver.quit()


def test_logout():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)

    driver.get(URL)
    wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys("standard_user")

    wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys("secret_sauce")
    wait.until(EC.visibility_of_element_located((By.NAME, 'login-button'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Open Menu']"))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Logout']"))).click()

    assert driver.current_url == URL

    driver.quit()



