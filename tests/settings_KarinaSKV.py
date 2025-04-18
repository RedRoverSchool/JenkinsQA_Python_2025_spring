from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import  json



BASE_URL = "https://www.saucedemo.com"

STANDARD_USER_NAME = "standard_user"
USER_PASSWORD = "secret_sauce"

@staticmethod
def autorizathion():

    driver = webdriver.Chrome()

    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(STANDARD_USER_NAME)
    driver.find_element(By.ID, "password").send_keys(USER_PASSWORD)
    driver.find_element(By.ID, "login-button").click()

@staticmethod
def check_autorizathion():

    assert "/inventory.html" in autorizathion().driver.current_url
    autorizathion().driver.quit()


BASE_URL2 = 'https://simple-books-api.glitch.me'
ENDPOINR_GET = f"{BASE_URL2}/status"

def get_method():
   responce  = requests.get(f"{ENDPOINR_GET}")
   print(responce.status_code)
   assert responce.status_code == 200, "Неверный статус кода. Получили: {responce.status_code}"

