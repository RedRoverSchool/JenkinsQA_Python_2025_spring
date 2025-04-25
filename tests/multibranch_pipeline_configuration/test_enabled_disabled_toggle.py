from conftest import logger
from tests.multibranch_pipeline_configuration.mbp_data import Data


def test_default_state_of_the_toggle(driver, toggle):
    assert toggle.text == Data.TOGGLE_ENABLED_TEXT, logger.error(Data.TOGGLE_ENABLED_ERROR_TEXT)
