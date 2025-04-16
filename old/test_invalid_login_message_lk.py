import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_invalid_login_message():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, 'username').send_keys("tomsmith")
    driver.find_element(By.ID, 'password').send_keys("it_is_wrongpassword")
    driver.find_element(By.CLASS_NAME, 'radius').click()
    time.sleep(3)
    message = driver.find_element(By.ID, 'flash')
    time.sleep(2)

    assert "Your password is invalid!" in message.text
