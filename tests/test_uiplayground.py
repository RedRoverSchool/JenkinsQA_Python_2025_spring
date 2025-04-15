import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

BASE_URL = "http://uitestingplayground.com"
button_name = "Cool button"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Or whatever browser you're using
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def playground(driver, base_url):
    yield driver

def test_scroll_non_visible_button(playground, base_url):
    playground.get(f"{base_url}/scrollbars")
    button = WebDriverWait(playground, 2).until(
        EC.presence_of_element_located((By.ID, "hidingButton"))
    )
    playground.execute_script("arguments[0].scrollIntoView();", button)

    button = WebDriverWait(playground, 2).until(
        EC.element_to_be_clickable((By.ID, "hidingButton"))
    )
    assert button.is_displayed(), "The button is not visible on the page."
    print("The button is visible.")
    button.click()

def test_entering_text(playground, base_url):
    playground.get(f"{base_url}/textinput")
    input_text_field = playground.find_element(By.ID, "newButtonName")
    input_text_field.send_keys(button_name)
    button = playground.find_element(By.ID, "updatingButton")
    original_text = button.text
    button.click()

    updated_button = playground.find_element(By.ID, "updatingButton")
    new_text = updated_button.text

    assert new_text == button_name
    assert new_text != original_text
    print(f"Button text was changed  from '{original_text}'   to '{button_name}'")