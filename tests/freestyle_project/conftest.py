import pytest

from tests.freestyle_project.freestyle_data import Freestyle
from pages.freestyle_project_config_page import FreestyleProjectConfigPage
from pages.main_page import MainPage
# from pages.freestyle_project_page import FreestyleProjectPage


@pytest.fixture
def freestyle(main_page):
    freestyle_config_page = MainPage(main_page).go_to_new_item_page().create_new_freestyle_project(Freestyle.project_name)
    freestyle_config_page.wait_for_element(FreestyleProjectConfigPage.Locator.H2, 10)

    return freestyle_config_page

# @pytest.fixture
# def tooltip(freestyle):
#     return freestyle.get_tooltip_enable().text

@pytest.fixture
def disabled_message(freestyle):
    freestyle.switch_to_disable()
    return freestyle.click_save_button().get_warning_message().splitlines()[0]

@pytest.fixture
def enable_automatically(freestyle):
    is_warning_message_disappear = False
    is_project_enable = False
    freestyle.switch_to_disable()
    project_page = freestyle.click_save_button()
    project_page.click_enable_button()
    if project_page.get_warning_message() == '':
        is_warning_message_disappear = True
    config_page = project_page.go_to_configure()
    if config_page.is_enable_text() == "Enabled":
        is_project_enable = True

    return [is_warning_message_disappear, is_project_enable]

