from selenium.webdriver.common.by import By
import time

def test_cart_icon_displays_correct_item_count(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='add-to-cart']").click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", f"Ожидалось '1' в корзине, но получено '{cart_badge.text}'"