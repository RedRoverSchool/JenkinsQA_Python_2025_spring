from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_burger_menu():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("visual_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "inventory_sidebar_link")
    sleep(0.5)

    assert driver.find_element(By.ID, "inventory_sidebar_link").text == "All Items"
