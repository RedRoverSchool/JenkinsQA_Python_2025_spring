from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_locked_out_user():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()

    # error_mesage = driver.find_element(By.XPATH, //)
    time.sleep(60)