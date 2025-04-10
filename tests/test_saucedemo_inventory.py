from selenium import webdriver
from selenium.webdriver.common.by import By


def test_add_inventory_to_shopping_cart():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("visual_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.CSS_SELECTOR, "#item_1_title_link > div").click()

    inventory_price = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price']").text
    inventory_details = inventory_price.split("$")
    inventory_details[0] = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-name']").text

    driver.find_element(By.ID, "add-to-cart").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    inventory_price_in_cart = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price']").text
    inventory_details_in_cart = inventory_price_in_cart.split("$")
    inventory_details_in_cart[0] = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-name']").text

    assert all([i1 == i2 for i1, i2 in zip(inventory_details, inventory_details_in_cart)])

    driver.quit()
