from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 3)
    base_url = 'https://www.saucedemo.com/'

    driver.get(base_url)

    user_name = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    user_name.send_keys("standard_user")

    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("secret_sauce")

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="title"]')))
    title = "Products"
    assert title == products.text, 'ОШИБКА, заголовок не совпадает'

    driver.quit()

