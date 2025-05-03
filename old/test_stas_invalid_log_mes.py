from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

URL = "https://practicetestautomation.com/practice-test-login/"

options = EdgeOptions()
service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)


def test_positive():
    try:
        driver.get(URL)
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        current_url = driver.current_url

        assert (
            current_url == "https://practicetestautomation.com/logged-in-successfully/"
        )
    finally:
        driver.quit()


def test_incorrect_user():
    try:
        driver.get(URL)
        driver.find_element(By.ID, "username").send_keys("IncorrectUser")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        wait = WebDriverWait(driver, 10)
        error_message = wait.until(EC.visibility_of_element_located((By.ID, "error")))

        assert error_message.text == "Your username is invalid!"
    finally:
        driver.quit()
