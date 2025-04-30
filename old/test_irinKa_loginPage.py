import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_page(driver):
    userName = "rahulshettyacademy"
    pw = "learning"

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.ID, "username").send_keys(userName)
    driver.find_element(By.ID, "password").send_keys(pw)

    dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
    dropdown.select_by_visible_text("Teacher")

    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "signInBtn").click()
    time.sleep(2)

    assert driver.current_url == "https://rahulshettyacademy.com/angularpractice/shop"
    assert "https://rahulshettyacademy.com/loginpagePractise/" not in driver.current_url
