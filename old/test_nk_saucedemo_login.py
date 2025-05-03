from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    driver.quit()
