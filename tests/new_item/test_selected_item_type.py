import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

def test_item_type_selection_sets_active_class(new_item_page):
        wait5 = WebDriverWait(new_item_page, 5)
        selected_type = wait5.until(
                EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'hudson_model_FreeStyleProject')]"))
        )
        selected_type.click()

        items = new_item_page.find_elements(By.CSS_SELECTOR, ".j-item-options li")
        assert selected_type.get_attribute("aria-checked") == "true" and not any(
                item != selected_type and item.get_attribute("aria-checked") == "true"
                for item in items
        )

