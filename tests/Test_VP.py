from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login():
    driver = webdriver.Chrome()

    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, 'login2').click()

    driver.find_element(By.ID, 'loginusername').send_keys("User_test007")
    driver.find_element(By.ID, 'loginpassword').send_keys("My_pswr_0912")
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="logIn()"]').click()
    assert driver.current_url == "https://www.demoblaze.com/", "wrong url"
    driver.quit()