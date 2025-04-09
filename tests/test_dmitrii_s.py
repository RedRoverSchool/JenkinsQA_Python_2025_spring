from selenium import webdriver
from selenium.webdriver.common.by import By

def test_locked_out_user_error_message_css():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("locked_out_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    error_element = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    error_text = error_element.text

    assert "Epic sadface: Sorry, this user has been locked out." in error_text, "Error message not found!"

    driver.quit()

def test_locked_out_user_error_message_xpath():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("locked_out_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    error_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    error_text = error_element.text

    assert "Epic sadface: Sorry, this user has been locked out." in error_text, "Error message not found!"

    driver.quit()

def test_error_user_price_item():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("error_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    price_element = driver.find_element(By.XPATH, "(//*[@data-test='inventory-item-price'])[2]")
    price_text = price_element.text

    assert price_text == "$9.99", f"Unexpected price: {price_text}"

    driver.quit()

def test_error_user_url_check():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("error_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "wrong url"

    driver.quit()
