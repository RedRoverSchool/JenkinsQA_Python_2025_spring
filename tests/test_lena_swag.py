from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, 'user-name').send_keys("standard_user")
    browser.find_element(By.ID, 'password').send_keys("secret_sauce")
    browser.find_element(By.NAME, 'login-button').click()
    yield browser
    browser.quit()


def test_logo(browser):
    assert "Swag Labs" in browser.title

def test_add_to_cart(browser):
    browser.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack').click()
    button_name = browser.find_element(By.NAME, 'remove-sauce-labs-backpack')
    shopping_cart = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert button_name.text == "Remove"
    assert shopping_cart.text == "1"


def test_price_sort_low_to_high(browser):
    select_element = Select(browser.find_element(By.CLASS_NAME, 'product_sort_container'))
    select_element.select_by_value('lohi')
    price_elements = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
    prices = []
    for price in price_elements:
        price_text = price.text.replace('$', '')
        prices.append(float(price_text))
    sorted_prices = sorted(prices)
    assert prices == sorted_prices, f"Prices are not sorted! Actual: {prices} Expected: {sorted_prices}"


def test_price_sort_high_to_low(browser):
    select_element = Select(browser.find_element(By.CLASS_NAME, 'product_sort_container'))
    select_element.select_by_value('hilo')
    price_elements = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
    prices = [float(price.text.replace('$', '')) for price in price_elements]
    sorted_prices = sorted(prices, reverse=True)
    assert prices == sorted_prices, f"Prices are not sorted correctly! Actual: {prices} Expected: {sorted_prices}"


