from selenium.webdriver.common.by import By
from tests.new_item.data_structs import NewItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_name_alphanumeric(driver, new_item_page):
    # Wait for the name text field to be visible
    wait = WebDriverWait(driver, timeout=5)
    name_field = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, NewItem.name_field_selector))
    )
    # Count all present validation errors before inserting any text
    all_validation_errors_before = new_item_page.find_elements(
        By.CSS_SELECTOR, NewItem.common_validation_error_selector
    )

    # Enter the text into the 'Enter an item name' text field
    name_field.send_keys(NewItem.positive_name)

    # Click outside the 'Enter an item name' text field
    page_name = new_item_page.find_element(By.XPATH, NewItem.page_name_selector)
    page_name.click()

    # Verify that no error appeared
    all_validation_errors_after = new_item_page.find_elements(
        By.CSS_SELECTOR, NewItem.common_validation_error_selector
    )
    assert len(all_validation_errors_before) == len(all_validation_errors_after), (
        NewItem.assert_message(
            message=" Number of expected disabled validation errors does not match."
        )
    )

    # Verify that the text is still present in the 'Enter an item name' text field
    assert name_field.get_attribute("value") == NewItem.positive_name, (
        NewItem.assert_message()
    )
