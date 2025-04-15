from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()
    yield driver


def test_logo(driver):
    assert "Swag Labs" in driver.title

def test_add_to_cart(driver):
    driver.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack').click()
    button_name = driver.find_element(By.NAME, 'remove-sauce-labs-backpack')
    shopping_cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert button_name.text == "Remove"
    assert shopping_cart.text == "1"

