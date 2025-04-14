import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# url = 'https://www.saucedemo.com/'
# username_standard = 'standard_user'
# password = 'secret_sauce'

def login_standard_user(driver, config, wait):
    driver.get(config.URL)
    wait.until(EC.presence_of_element_located((By.ID, 'user-name'))).send_keys(config.USER)
    driver.find_element(By.ID, 'password').send_keys(config.PASSWORD)
    driver.find_element(By.ID, 'login-button').click()

def test_standard_user_login(driver, config, wait):
    login_standard_user(driver, config, wait)
    print("user:", config.USER)
    print("password:", config.PASSWORD)
    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url

def test_standard_user_title(driver, config, wait):
    expected_title = "Products"
    login_standard_user(driver, config, wait)
    title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-test='title']")))
    assert title.text == expected_title, (f'expected result {expected_title} but got {title.text}')

def test_product_add(driver, config, wait):
    basket_logo = '1'
    login_standard_user(driver, config, wait)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack"))).click()
    basket_lago = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#shopping_cart_container"))).click()
    item_count = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test='item-quantity']"))).text
    assert item_count == basket_logo,(f"ecpected result {basket_lago}, bot got {item_count}")