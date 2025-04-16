import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_sort_products_by_price(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


    sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_dropdown.click()

    sort_option = driver.find_element(By.XPATH, "//option[text()='Price (low to high)']")
    sort_option.click()

    time.sleep(5)

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_values = []
    for price in prices:
        price_text = price.text
        if "$" in price_text:
            price_text = price_text.replace("$", "")
        price_values.append(float(price_text))

    assert price_values == sorted(price_values), "Products are not sorted by price from low to high"