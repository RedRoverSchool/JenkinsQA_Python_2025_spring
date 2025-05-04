from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.freestyle_project.freestyle_data import Freestyle
from pages.freestyle_project_config_page import FreestyleProjectConfigPage
from pages.main_page import MainPage


# def test_enable_disable_switch(freestyle):
#
#     assert freestyle.is_enable().is_displayed()
#
#     freestyle.switch_to_disable()
#     assert freestyle.is_disable().is_displayed()

# def test_tooltip(tooltip):
#
#     assert tooltip == Freestyle.tooltip_disable
#
# def test_disabled_message(disabled_message):
#
#     assert disabled_message == Freestyle.warning_message
#
def test_enable_after_disabled(enable_automatically):

    assert enable_automatically[0] and enable_automatically[1]
