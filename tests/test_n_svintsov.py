from selenium import webdriver
from selenium.webdriver.common.by import By



def test_locked_out_user_error_message():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."
    driver.quit()

def test_locked_out_user_url_check():
        driver = webdriver.Chrome()

        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()

        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error_message.text == "Epic sadface: Sorry, this user has been locked out."

        assert driver.current_url == "https://www.saucedemo.com/","wrong url"
        driver.quit()


def test_locked_out_user_url_check():
    with webdriver.Chrome() as driver:

        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()

        assert driver.current_url == "https://www.saucedemo.com/", "wrong url"

