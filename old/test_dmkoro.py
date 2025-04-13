from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_success():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    #driver.find_element(By.CSS_SELECTOR, "button.radius[type='submit']").click()
    driver.find_element(By.TAG_NAME, "button").click()

    login_confirmation_text = driver.find_element(By.ID, "flash").text
    assert login_confirmation_text == "You logged into a secure area!\n×"

    driver.quit()



