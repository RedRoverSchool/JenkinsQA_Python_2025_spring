import os
from dotenv import load_dotenv
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

def click_new_item_button(driver):
    try:
        new_item_button = driver.find_element(By.XPATH, "//a[contains(@href, '/newJob')]")
        new_item_button.click()
    except NoSuchElementException:
        raise AssertionError(
            "The 'New Item' button was not found. Please check localization or changes in the Jenkins UI.")

@pytest.mark.usefixtures("driver")
class TestNewItemSpecialCharacters:

    def test_special_characters_not_allowed(self, login_page, main_page, driver):
        assert login_page.title == "Sign in [Jenkins]" or main_page.title in ["Dashboard [Jenkins]", "ИнфоПанель [Jenkins]"]

        click_new_item_button(driver)

        invalid_name = "Invalid!@#$%"
        name_input = driver.find_element(By.ID, "name")
        name_input.send_keys(invalid_name)

        wait = WebDriverWait(driver, 20)

        wait.until(lambda d: not d.find_element(By.ID, "ok-button").is_enabled())

        error_element = wait.until(
            EC.visibility_of_element_located((By.ID, "itemname-invalid"))
        )

        text = error_element.text.strip().lower()
        assert "unsafe character" in text, f"Expected 'unsafe character' in the error message, but got: '{text}'"
#