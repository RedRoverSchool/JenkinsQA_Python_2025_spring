from selenium import webdriver
from selenium.webdriver.common.by import By


def test_success_log_in():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.XPATH, "//*[@id='login-button']").click()

    assert "inventory" in driver.current_url

    driver.quit()


def test_locked_out_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    assert (
        driver.find_element(By.XPATH, '//*[@ data-test="error"]').text
        == "Epic sadface: Sorry, this user has been locked out."
    )

    driver.quit()


def test_empty_fields():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name")
    driver.find_element(By.ID, "password")

    driver.find_element(By.ID, "login-button").click()

    assert driver.find_element(By.XPATH, '//*[@Data-test="error"]')

    driver.quit()
