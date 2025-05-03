from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.new_item_page import NewItemPage
from tests.new_item.data import new_folder_name, new_freestyle_project_name
import pytest

# from tests_to_refactor.freestyle_project.conftest import freestyle


@pytest.mark.skip
def test_build_steps_availability2(new_item_page: NewItemPage):
    folder_config_page = new_item_page.create_new_folder(new_freestyle_project_name)
    folder_config_page.wait_for_url()
    items = folder_config_page.go_to_the_main_page().get_item_list()
    assert items == [new_folder_name], f"Folder '{new_folder_name}' NOT FOUND"


def test_build_steps_availability(new_item_page: NewItemPage):
    freestyle_project_config_page = new_item_page.create_new_freestyle_project(
        new_freestyle_project_name
    )
    freestyle_project_config_page.wait_for_url()

    add_build_step_button = freestyle_project_config_page.find_element(
        By.XPATH,
        "//button[@class='jenkins-button hetero-list-add' and @suffix='builder']",
    )
    add_build_step_button.send_keys(Keys.END)
    add_build_step_button.click()

    build_steps_locator = (By.XPATH, "//button[@class='jenkins-dropdown__item ']")
    freestyle_project_config_page.wait_to_be_clickable(build_steps_locator)
    build_steps_we = freestyle_project_config_page.find_elements(*build_steps_locator)

    build_steps_items = {el.text for el in build_steps_we}
    expected_items = {
        "Execute Windows batch command",
        "Execute shell",
        "Invoke Ant",
        "Invoke Gradle script",
        "Invoke top-level Maven targets",
        "Run with timeout",
        'Set build status to "pending" on GitHub commit',
    }

    assert expected_items == build_steps_items
