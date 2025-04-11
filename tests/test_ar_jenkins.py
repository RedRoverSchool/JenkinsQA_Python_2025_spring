import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_to_jenkins():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/")
    driver.find_element(By.ID, "j_username").send_keys("Andrei")
    driver.find_element(By.ID, "j_password").send_keys("123456Andrei!")
    driver.find_element(By.NAME, "Submit").click()
    assert driver.find_element(By.ID, "jenkins-head-icon")
    driver.quit()

def test_wrong_username_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/")
    driver.find_element(By.ID, "j_username").send_keys("And")
    driver.find_element(By.ID, "j_password").send_keys("123456Andrei!")
    driver.find_element(By.NAME, "Submit").click()
    assert driver.current_url == "http://localhost:8080/loginError"
    driver.quit()

def test_wrong_password_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/")
    driver.find_element(By.ID, "j_username").send_keys("Andrei")
    driver.find_element(By.ID, "j_password").send_keys("123456")
    driver.find_element(By.NAME, "Submit").click()
    time.sleep(2)
    error = driver.find_element(By.CLASS_NAME, "app-sign-in-register__error")
    assert "Invalid username or password" in error.text
    driver.quit()
