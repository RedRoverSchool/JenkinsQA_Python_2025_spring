from tests.new_item.data_structs import NewItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_special_chars_validation_error(new_item_page):
    wait = WebDriverWait(new_item_page, timeout=5)
    name_field = wait.until(
        EC.visibility_of_element_located(NewItem.name_field_selector)
    )
    any_errors_before = new_item_page.find_elements(*NewItem.any_enabled_error)

    assert not any_errors_before, (
        "Validation error appears even before interacting with the Item name field"
    )

    page_name = new_item_page.find_element(*NewItem.page_name_selector)
    for char in NewItem.special_chars:
        name_field.send_keys(char)
        page_name.click()
        any_errors_after = wait.until(
            EC.visibility_of_all_elements_located(NewItem.any_enabled_error)
        )

        assert len(any_errors_after) == 1, (
            f"Unexpected number of errors detected after inserting {char}"
        )

        expected_error_text = f"» ‘{char}’ is an unsafe character"
        wait.until(
            EC.text_to_be_present_in_element(
                NewItem.any_enabled_error, expected_error_text
            )
        )
        name_field.clear()
