from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_to_cart_item():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed"

    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
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

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/cart.html", "Not on cart page"

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    cart_item_name = []
    cart_item_description = []
    cart_item_price = []
    for cart_item in cart_items:
        cart_item_name.append(cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text)
        cart_item_price.append(cart_item.find_element(By.CLASS_NAME, "inventory_item_price").text)
        cart_item_description.append(cart_item.find_element(By.CLASS_NAME, "inventory_item_desc").text)

    assert len(items) == len(cart_items), f"{len(items)} should be equal {len(cart_items)}"

    for index in range(len(cart_item_name)):
        assert item_name[index] == cart_item_name[index], "Wrong item name in cart"

    for index in range(len(cart_item_description)):
        assert item_description[index] == cart_item_description[index], "Wrong item description in cart"

    for index in range(len(cart_item_price)):
        assert item_price[index] == cart_item_price[index], "Wrong item price in cart"

    driver.quit()
