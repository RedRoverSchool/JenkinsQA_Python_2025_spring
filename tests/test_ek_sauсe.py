import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def browser_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--incognito")
    return options

@pytest.fixture(scope="module")
def driver(browser_options):
    driver = webdriver.Chrome(options=browser_options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def authorization(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    return driver

@pytest.fixture(scope="function")
def clean_cart(authorization):
    driver = authorization
    driver.get("https://www.saucedemo.com/cart.html")
    try:
        while True:
            remove_cart = driver.find_element(By.XPATH, "//button[text()='Remove']")
            remove_cart.click()
    except:
        pass
    driver.get("https://www.saucedemo.com/inventory.html")
    yield driver



def test_add_to_cart(clean_cart):
        clean_cart.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        clean_cart.get("https://www.saucedemo.com/cart.html")
        item = clean_cart.find_element(By.XPATH, "//div[contains(@class, 'inventory_item_name')]")
        count = clean_cart.find_element(By.XPATH, "//div[@data-test='item-quantity']")
        assert item.text == "Sauce Labs Backpack" and count.text == "1", "The product has not been added to the cart"


def test_remove_from_cart(clean_cart):
    clean_cart.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    clean_cart.get("https://www.saucedemo.com/cart.html")
    clean_cart.find_element(By.ID, "remove-sauce-labs-backpack").click()
    removed_cart = clean_cart.find_element(By.XPATH, "//div[contains(@class, 'removed_cart_item')]")
    assert removed_cart is not None, "The product has not been removed from the cart"
