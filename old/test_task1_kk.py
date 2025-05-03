import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://practicetestautomation.com/practice-test-login/"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 5)


def test_login_with_valid_creds(driver, wait):
    driver.get(URL)

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.XPATH, "//button[@class='btn']").click()

    wait.until(
        EC.url_to_be("https://practicetestautomation.com/logged-in-successfully/")
    )
    assert (
        driver.current_url
        == "https://practicetestautomation.com/logged-in-successfully/"
    ), "URL is invalid!"

    welcome_header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    assert welcome_header.text == "Logged In Successfully", "Something went wrong"

    logout_button = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Log out"))
    )
    assert logout_button.is_displayed(), "Log out button is not displayed!"


def test_login_invalid_username(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "username").send_keys("incorrectUser")
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.XPATH, "//button[@class='btn']").click()

    error_message = wait.until(EC.visibility_of_element_located((By.ID, "error")))
    assert error_message.is_displayed(), "Error message is not displayed!"
    assert error_message.text == "Your username is invalid!", (
        "Unexpected error message!"
    )
