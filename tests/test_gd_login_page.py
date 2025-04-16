import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def sauce(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_login_back_login_page_opens(sauce):
    sauce.find_element(By.ID, "user-name").send_keys("standard_user")
    sauce.find_element(By.ID, "password").send_keys("secret_sauce")
    sauce.find_element(By.ID, "login-button").click()
    sauce.back()
    title = sauce.find_element(By.XPATH, "//*[@class = 'login_logo']").text

    assert title == "Swag Labs"


def test_error_appears_and_disappears_after_refresh_login_page(sauce):
    sauce.find_element(By.ID, "login-button").click()
    error_el = sauce.find_elements(By.XPATH, "//*[contains(text(),'Username is required')]")

    assert len(
        error_el) == 1, "Error message is not showing or there are more than one error messages"

    sauce.refresh()
    error_el_after_refresh = sauce.find_elements(By.XPATH, "//*[contains(text(),'Username is required')]")

    assert len(error_el_after_refresh) == 0, "Error message is still showing after page refresh"
