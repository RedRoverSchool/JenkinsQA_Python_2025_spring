from selenium import webdriver
from selenium.webdriver.common.by import By


def test_locked_out_user():
    driver = webdriver.Chrome()
    where = "on the login page"

    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.CSS_SELECTOR, "#user-name")
    username.send_keys("locked_out_user")

    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys("secret_sauce")

    login_btn = driver.find_element(By.CSS_SELECTOR, "#login-button")
    login_btn.click()

    expected_error_msg = "Epic sadface: Sorry, this user has been locked out."
    error_button = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    found_error_msg = error_button.text

    assert error_button.is_displayed(), f"Error button is not displayed {where}"
    assert found_error_msg == expected_error_msg, (
        f"Incorrect error message found {where}. Found text was: {found_error_msg}"
    )
