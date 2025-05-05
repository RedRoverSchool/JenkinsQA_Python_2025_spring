from selenium.webdriver.support import expected_conditions as EC

from .data_structs import NewItem, CopyFrom


def test_display_existing_item(prepare_new_item, config, wait5):
    prepare_new_item.find_element(*CopyFrom.copy_from_selector).send_keys(
        CopyFrom.first_letter_of_name()
    )
    item_element = wait5.until(EC.visibility_of_element_located(
        CopyFrom.dropdown_item_selector)
    )
    actual_text = item_element.text.strip()

    assert actual_text == NewItem.positive_name, (
        f"Expected item '{NewItem.positive_name}', but found '{actual_text}'"
    )
