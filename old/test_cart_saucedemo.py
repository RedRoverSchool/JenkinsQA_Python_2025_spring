from selenium import webdriver
from selenium.webdriver.common.by import By


base_url = "https://www.saucedemo.com/"
user_name = "standard_user"
psw = "secret_sauce"


def login(driver, username, password):
    """Logs in to the app with given credentials."""
    driver.get(base_url)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def fill_checkout_information(driver, first_name, last_name, postal_code):
    """Fills in the checkout form with user info."""
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    driver.find_element(By.ID, "continue").click()


def test_add_product_to_cart():
    """Verifies that a user can log in, add a product to the cart, and see the cart badge."""
    driver = webdriver.Chrome()
    login(driver, user_name, psw)

    driver.find_element(By.ID, "item_4_title_link").click()
    driver.find_element(By.ID, "add-to-cart").click()

    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").is_displayed()

    driver.quit()


def test_added_products_in_cart():
    """Verifies that the specific products are in the cart."""
    expected_products = ["Sauce Labs Backpack", "Sauce Labs Onesie"]

    driver = webdriver.Chrome()
    login(driver, user_name, psw)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    cart_item_names = [item.text for item in cart_items]

    assert len(cart_items) == 2, (
        f"Expected 2 items in the cart, but found {len(cart_items)}."
    )
    for product in expected_products:
        assert product in cart_item_names, f"{product} was not found in the cart."

    driver.quit()


def test_products_displayed_in_checkout():
    """Verifies that added products are displayed correctly during checkout."""
    expected_products = ["Sauce Labs Backpack", "Sauce Labs Onesie"]

    driver = webdriver.Chrome()
    login(driver, user_name, psw)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    fill_checkout_information(driver, "Test", "User", "12345")

    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    actual_product_names = [element.text for element in product_elements]

    assert len(product_elements) == 2, (
        f"Expected 2 items in the cart, but found {len(product_elements)}."
    )
    for product in expected_products:
        assert product in actual_product_names, (
            f"'{product}' not found on checkout page."
        )

    driver.quit()
