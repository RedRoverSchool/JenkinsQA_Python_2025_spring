import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def dynamic_id(driver):
    driver.get("http://uitestingplayground.com/dynamicid")
    return driver


def test_dynamic_id_button(dynamic_id):
    button = dynamic_id.find_element(
        By.XPATH, "//button[contains(text(),'Button with Dynamic ID')]"
    )
    button_id = button.get_attribute("id")
    button.click()
    dynamic_id.refresh()
    refreshed_button = dynamic_id.find_element(
        By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]"
    )
    refreshed_button_id = refreshed_button.get_attribute("id")
    refreshed_button.click()

    assert refreshed_button.is_displayed(), (
        "The button with dynamic ID is not visible after refresh"
    )
    assert button_id != refreshed_button_id, "Button ID did not change"
