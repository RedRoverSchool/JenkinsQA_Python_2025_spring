from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert


def test_login_incorrect_password():
    driver = webdriver.Chrome()

    driver.get("https://www.demoblaze.com/")
    element_login = driver.find_element(By.ID, "login2")
    driver.execute_script("arguments[0].click();", element_login)

    element_modal = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.ID, "logInModal"))
    )
    assert element_modal.is_displayed(), "Element is not displayed"

    driver.find_element(By.ID, "loginusername").send_keys("test")
    driver.find_element(By.ID, "loginpassword").send_keys("password")
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())
    assert Alert(driver).text == "Wrong password."

    driver.quit()
