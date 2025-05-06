from tests.new_item.data_structs import NewItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_name_alphanumeric(new_item_page):
    wait = WebDriverWait(new_item_page, timeout=5)
    name_field = wait.until(
        EC.visibility_of_element_located(NewItem.name_field_selector)
    )
    all_validation_errors_before = new_item_page.find_elements(
        *NewItem.common_validation_error_selector
    )

    name_field.send_keys(NewItem.positive_name)
    page_name = new_item_page.find_element(*NewItem.page_name_selector)
    page_name.click()
    all_validation_errors_after = new_item_page.find_elements(
        *NewItem.common_validation_error_selector
    )

    assert len(all_validation_errors_before) == len(all_validation_errors_after), (
        "Not all validation errors were disabled."
    )
    assert name_field.get_attribute("value") == NewItem.positive_name, (
        "The positive Item name did not stay in the field."
    )
