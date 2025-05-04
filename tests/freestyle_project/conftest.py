import pytest

from tests.freestyle_project.freestyle_data import Freestyle
from pages.freestyle_project_config_page import FreestyleProjectConfigPage


@pytest.fixture
def freestyle(main_page):
    freestyle_config_page = main_page.go_to_new_item_page().create_new_freestyle_project(Freestyle.project_name)
    freestyle_config_page.wait_for_element(FreestyleProjectConfigPage.Locator.H2_LOCATOR, 10)
    return freestyle_config_page

@pytest.fixture
def tooltip(freestyle: FreestyleProjectConfigPage):
    return freestyle.get_tooltip(Freestyle.tooltip_enable, Freestyle.tooltip_enable_wait)

@pytest.fixture
def disabled_message(freestyle):
    freestyle.switch_to_disable()
    return freestyle.click_save_button().get_warning_message().splitlines()[0]

@pytest.fixture
def enable_automatically(freestyle: FreestyleProjectConfigPage):
    from pages.freestyle_project_page import FreestyleProjectPage
    freestyle.switch_to_disable()
    project_page: FreestyleProjectPage = freestyle.click_save_button()
    project_page.wait_text_to_be_present(FreestyleProjectPage.Locator.H1, Freestyle.project_name)
    project_page.click_enable_button()
    if project_page.get_warning_message() == '':
        is_warning_message_disappear = True
    else:
        is_warning_message_disappear = False
    project_config = project_page.go_to_configure()
    if project_config.is_enable().is_displayed():
        is_project_enable = True
    else:
        is_project_enable = False
    return [is_warning_message_disappear, is_project_enable]
