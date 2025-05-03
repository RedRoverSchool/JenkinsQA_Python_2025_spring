from selenium.webdriver import ActionChains

from conftest import logger
from tests.multibranch_pipeline_configuration.mbp_data import Data


def test_default_state_of_the_toggle(driver, toggle):
    assert toggle.text == Data.TOGGLE_ENABLED_TEXT, logger.error(
        Data.TOGGLE_ENABLED_ERROR_TEXT
    )


def test_the_tooltip_appearance(driver, toggle, toggle_tooltip, span_general):
    action = ActionChains(driver)
    action.move_to_element(toggle_tooltip).perform()
    first_hovering = (
        toggle_tooltip.get_attribute(Data.TOGGLE_TOOLTIP_ATR[0]),
        toggle_tooltip.get_attribute(Data.TOGGLE_TOOLTIP_ATR[1]),
    )
    toggle.click()
    action.move_to_element(span_general).perform()
    action.move_to_element(toggle_tooltip).perform()
    second_hovering = (
        toggle_tooltip.get_attribute(Data.TOGGLE_TOOLTIP_ATR[0]),
        toggle_tooltip.get_attribute(Data.TOGGLE_TOOLTIP_ATR[1]),
    )

    assert Data.TOGGLE_TOOLTIP_PREFS == first_hovering == second_hovering, logger.error(
        Data.TOGGLE_TOOLTIP_ERROR_TEXT
    )
