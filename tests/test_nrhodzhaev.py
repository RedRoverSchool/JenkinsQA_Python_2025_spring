from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_cart_icon_displays_correct_item_count():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Логин
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Выбираем товар
    driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").click()
    time.sleep(2)

    # Добавляем товар в корзину
    driver.find_element(By.XPATH, "//*[@id='add-to-cart']").click()

    # Проверяем счетчик в корзине
    cart_badge = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a/span")
    assert cart_badge.text == "1", f"Ожидалось '1' в корзине, но получено '{cart_badge.text}'"

    driver.quit()


