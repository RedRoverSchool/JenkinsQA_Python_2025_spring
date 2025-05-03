from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    title = driver.find_element(By.XPATH, "//div//span[@data-test='title']").text
    assert title == "Products"
    driver.quit()


def test_wrong_username():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("non-standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(
        By.XPATH, "//*[contains(text(),'Username and password do not match any user')]"
    )
    assert "Username and password do not match any user in this service" in error.text
    driver.quit()


def test_wrong_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("non-secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(
        By.XPATH, "//*[contains(text(),'Username and password do not match any user')]"
    )
    assert "Username and password do not match any user in this service" in error.text
    driver.quit()


def test_empty_username():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(
        By.XPATH, "//*[contains(text(),'Username is required')]"
    )
    assert "Username is required" in error.text
    driver.quit()


def test_empty_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(
        By.XPATH, "//*[contains(text(),'Password is required')]"
    )
    assert "Password is required" in error.text
    driver.quit()
