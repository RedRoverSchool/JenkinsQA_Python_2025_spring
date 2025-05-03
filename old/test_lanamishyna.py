from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_cart_button():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("visual_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
    sleep(0.5)

    assert driver.current_url == "https://www.saucedemo.com/cart.html", "wrong url"
    driver.quit()


def test_cart_shopping_cart_badge():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("error_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    sleep(0.5)

    shopping_cart_badge = driver.find_element(By.ID, "shopping_cart_container")
    assert shopping_cart_badge.text == "1"
    driver.quit()
