from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def sauce_site(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_shopping_cart(sauce_site):
    sauce_site.find_element(By.ID, "user-name").send_keys("standard_user")
    sauce_site.find_element(By.ID, "password").send_keys("secret_sauce")
    sauce_site.find_element(By.ID, "login-button").click()

    item = sauce_site.find_element(By.XPATH, "//div[.='Sauce Labs Backpack']")
    item.click()
    sauce_site.find_element(By.NAME, "add-to-cart").click()
    sauce_site.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    item_in_cart = sauce_site.find_element(
        By.XPATH, "//div[@Data-test='inventory-item-name']"
    )

    assert item_in_cart.text == "Sauce Labs Backpack", (
        "Добавленный товар отсутствует в корзине"
    )
