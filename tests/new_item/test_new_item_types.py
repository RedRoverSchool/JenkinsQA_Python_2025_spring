from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.new_item_page import NewItemPage


def test_available_project_types_displayed(main_page, new_item_page):
    new_item_page.wait_for_url()

    expected_items = [
        "Freestyle project",
        "Pipeline",
        "Multi-configuration project",
        "Folder",
        "Multibranch Pipeline",
        "Organization Folder"
    ]

    displayed_items = new_item_page.get_item_type_names()
    assert displayed_items, "No project types are displayed on the page"

    for item in expected_items:
        assert item in displayed_items, f"Project type '{item}' not displayed"
