import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_until_visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def test_verify_unsuccessful_login(driver):
    driver.get("http://localhost:8080")
    driver.maximize_window()

    wait_until_visible(driver, (By.ID, "j_username")).send_keys("1234")
    wait_until_visible(driver, (By.ID, "j_password")).send_keys("1234")
    wait_until_visible(driver,(By.CSS_SELECTOR, "[name='Submit']")).click()

    actual_text = wait_until_visible(driver, (By.CSS_SELECTOR, ".app-sign-in-register__error")).text
    expected_text = "Invalid username or password"

    assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"