from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_scroll_non_visible_button(driver):
    driver.get("http://uitestingplayground.com/scrollbars")
    button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "hidingButton"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button)

    assert button.is_displayed(), "The button is not visible on the page."
    assert button.is_enabled(), "The button is not enabled"


def test_entering_text(driver):
    button_name = "Cool button"

    driver.get("http://uitestingplayground.com/textinput")
    input_text_field = driver.find_element(By.ID, "newButtonName")
    input_text_field.send_keys(button_name)
    button = driver.find_element(By.ID, "updatingButton")
    original_text = button.text
    button.click()

    updated_button = driver.find_element(By.ID, "updatingButton")
    new_text = updated_button.text

    assert new_text == button_name
    assert new_text != original_text
