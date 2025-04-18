import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.fixture
def standart_user_log_in(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    return driver

def add_items_to_cart(standart_user_log_in):
    items = standart_user_log_in.find_elements(By.CLASS_NAME, "inventory_item")

    item_name = []
    item_price = []
    item_description = []
    for item in items:
        item_name.append(item.find_element(By.CLASS_NAME, "inventory_item_name").text)
        item_price.append(item.find_element(By.CLASS_NAME, "inventory_item_price").text)
        item_description.append(item.find_element(By.CLASS_NAME, "inventory_item_desc").text)

        add_button = item.find_element(By.CLASS_NAME, "btn_inventory")
        add_button.click()
        time.sleep(1)
    return items, item_name, item_price, item_description

def items_in_cart(standart_user_log_in):
    standart_user_log_in.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_items = standart_user_log_in.find_elements(By.CLASS_NAME, "cart_item")
    cart_item_name = []
    cart_item_price = []
    cart_item_description = []
    for cart_item in cart_items:
        cart_item_name.append(cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text)
        cart_item_price.append(cart_item.find_element(By.CLASS_NAME, "inventory_item_price").text)
        cart_item_description.append(cart_item.find_element(By.CLASS_NAME, "inventory_item_desc").text)
    return cart_items, cart_item_name, cart_item_price, cart_item_description




def test_success_login_url(standart_user_log_in):
    assert standart_user_log_in.current_url == "https://www.saucedemo.com/inventory.html", "Login failed"

def test_same_item_numbers(standart_user_log_in):
    items, item_names, item_prices, item_description = add_items_to_cart(standart_user_log_in)
    cart_items, cart_item_names, cart_item_prices, cart_item_description = items_in_cart(standart_user_log_in)
    assert len(items) == len(cart_items), f"{len(items)} should be equal {len(cart_items)}"

def test_correct_cart_page(standart_user_log_in):
    standart_user_log_in.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert standart_user_log_in.current_url == "https://www.saucedemo.com/cart.html", "Not on cart page"

def test_same_item_names(standart_user_log_in):
    items, item_names, item_prices, item_description = add_items_to_cart(standart_user_log_in)
    cart_items, cart_item_names, cart_item_prices, cart_item_description = items_in_cart(standart_user_log_in)
    for index in range(len(cart_item_names)):
        assert item_names[index] == cart_item_names[index], "Wrong item name in cart"

def test_same_item_prices(standart_user_log_in):
    items, item_names, item_prices, item_description = add_items_to_cart(standart_user_log_in)
    cart_items, cart_item_names, cart_item_prices, cart_item_description = items_in_cart(standart_user_log_in)
    for index in range(len(cart_item_prices)):
        assert item_prices[index] == cart_item_prices[index], "Wrong item description in cart"

def test_same_item_descriptions(standart_user_log_in):
    items, item_names, item_prices, item_description = add_items_to_cart(standart_user_log_in)
    cart_items, cart_item_names, cart_item_prices, cart_item_description = items_in_cart(standart_user_log_in)
    for index in range(len(cart_item_description)):
        assert item_description[index] == cart_item_description[index], "Wrong item price in cart"

