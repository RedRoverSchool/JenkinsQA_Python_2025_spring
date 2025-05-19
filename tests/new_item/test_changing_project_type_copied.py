import pytest
from selenium.webdriver.common.by import By

from core.settings import Config
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.new_item_page import NewItemPage


@pytest.fixture
def new_project(driver):
    login_page = LoginPage(driver).open()
    creds = Config.load().jenkins
    main_page = login_page.login(creds.USERNAME, creds.PASSWORD)

    new_item_page = main_page.go_to_new_item_page()
    project_name = "NewProject"
    config_page = new_item_page.create_new_freestyle_project(project_name)
    config_page.click_save_button()

    folder_page = config_page.header.go_to_the_main_page()
    folder_page.wait_text_to_be_present((By.LINK_TEXT, project_name), project_name)

    return folder_page, project_name


def test_ok_button_enabled(new_project):
    folder_page, project_name = new_project

    new_item_page = folder_page.go_to_new_item_page()
    new_item_page.enter_copy_from(project_name)
    new_item_page.enter_item_name(f"{project_name}Copy")

    assert new_item_page.wait_to_be_clickable(new_item_page.Locators.OK_BUTTON).is_enabled(), "OK button is not enabled"


def test_empty_copy_from_field(new_project):
    folder_page, project_name = new_project

    new_item_page = folder_page.go_to_new_item_page()

    new_item_page.enter_copy_from(project_name)

    new_item_page.enter_item_name(f"{project_name}Copy")

    element = new_item_page.find_element(By.XPATH, "/html/body/div[3]/div/div/form/div[2]/div[2]/div[1]/ul/li[2]")
    element.click()

    assert new_item_page.get_value(new_item_page.Locators.COPY_FROM) == "", "Copy from field not empty"

    assert new_item_page.wait_to_be_clickable(new_item_page.Locators.OK_BUTTON).is_enabled(), "OK button is unexpectedly disabled"