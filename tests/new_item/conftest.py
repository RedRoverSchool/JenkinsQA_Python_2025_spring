import pytest
from selenium.webdriver.common.by import By
from tests.new_item.data_structs import NewItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Open New Item page
@pytest.fixture()
def new_item_page(main_page, config):
    # Dashboard is open. Clink on the New Item button
    new_item_button = main_page.find_element(
        By.CSS_SELECTOR, NewItem.new_item_button_selector
    )
    new_item_button.click()

    # Wait for the New Item page to be opened
    wait = WebDriverWait(main_page, 5)
    wait.until(EC.url_matches(config.jenkins.base_url + NewItem.url))

    return main_page
