from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

USER_NAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def user_login(driver, user_name, password):
    driver.find_element(By.ID,"user-name").send_keys(user_name)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def test_add_items_to_cart(driver):
    user_login(driver, USER_NAME, PASSWORD)

    add_buttons_list = driver.find_elements(By.XPATH, "//div[@data-test='inventory-list']//button")
    for add_button in add_buttons_list:
        add_button.click()

    driver.find_element(By.CSS_SELECTOR, "a[data-test='shopping-cart-link']").click()
    cart_items_list = driver.find_elements(By.CLASS_NAME, "cart_item_label")

    assert len(add_buttons_list) == len(cart_items_list)

def test_remove_item_from_cart(driver):
    user_login(driver, USER_NAME, PASSWORD)

    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "a[data-test='shopping-cart-link']").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    cart_items_list = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items_list) == 0
