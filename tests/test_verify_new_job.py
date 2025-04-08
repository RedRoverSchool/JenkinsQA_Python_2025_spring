from selenium import webdriver
from selenium.webdriver.common.by import By


def test_unseccess_login():
    driver = webdriver.Chrome()

    driver.get("http://localhost:8080")
    driver.maximize_window()

    driver.implicitly_wait(5)

    driver.find_element(By.ID, "j_username").send_keys("1234")
    driver.find_element(By.ID, "j_password").send_keys("1234")
    driver.find_element(By.CSS_SELECTOR, "[name='Submit']").click()

    assert driver.find_element(By.CSS_SELECTOR, ".app-sign-in-register__error").text == "Invalid username or password"
