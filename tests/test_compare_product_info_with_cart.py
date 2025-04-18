import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def target(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_compare_product_info_with_cart(driver, target):
    driver.find_element(By.ID, "user-name").send_keys("visual_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.CSS_SELECTOR, "#item_1_title_link > div").click()

    prd_price = target.find_element(By.XPATH, "//div[@data-test='inventory-item-price']").text
    prd_details = prd_price.split("$")
    prd_details[0] = target.find_element(By.XPATH, "//div[@data-test='inventory-item-name']").text
    prd_details.append(target.find_element(By.XPATH, "//div[@data-test='inventory-item-desc']").text)

    driver.find_element(By.ID, "add-to-cart").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    prd_price_in_cart = target.find_element(By.XPATH, "//div[@data-test='inventory-item-price']").text
    prd_details_in_cart = prd_price_in_cart.split("$")
    prd_details_in_cart[0] = target.find_element(By.XPATH, "//div[@data-test='inventory-item-name']").text
    prd_details_in_cart.append(target.find_element(By.XPATH, "//div[@data-test='inventory-item-desc']").text)

    assert all([i1 == i2 for i1, i2 in zip(prd_details, prd_details_in_cart)]), \
        "The product details in the product card do not match those in the shopping cart."
