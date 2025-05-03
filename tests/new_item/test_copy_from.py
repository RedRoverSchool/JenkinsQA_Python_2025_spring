from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from .data_structs import FreestyleItem, NewItem
from .new_item_steps import create_freestyle_item


def test_copy_from_dropdown_shows_existing_item(new_item_page, config):
    wait = WebDriverWait(new_item_page, 10)
    new_item_page = create_freestyle_item(new_item_page, config)
    new_item_page.find_element(*FreestyleItem.copy_from_field_selector).send_keys(
        FreestyleItem.get_first_letter_of_project_name()
    )
    existing_item = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@class, 'jenkins-dropdown__item')]")
        )
    )
    actual_item_text = existing_item.text.strip()
    assert actual_item_text == NewItem.positive_name, (
        f"Expected item '{NewItem.positive_name}', but found '{actual_item_text}'"
    )
