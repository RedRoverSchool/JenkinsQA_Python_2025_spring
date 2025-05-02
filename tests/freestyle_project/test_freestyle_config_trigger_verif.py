from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from tests.freestyle_project.data import TRIGGER_OPT_NAMES

def test_trigger_section(freestyle):
    title_triggers = freestyle.find_element(By.ID, 'triggers')
    assert title_triggers.is_displayed

@pytest.mark.parametrize("t_name", TRIGGER_OPT_NAMES)
def test_each_trigger_opt_enable(freestyle, t_name):
    el = freestyle.find_element(By.NAME, t_name)
    el.send_keys(Keys.SPACE)
    assert el.is_selected(), f"{t_name} should be enabled"

@pytest.mark.parametrize("t_name", TRIGGER_OPT_NAMES)
def test_each_trigger_opt_disable(freestyle, t_name):
    el = freestyle.find_element(By.NAME, t_name)
    el.send_keys(Keys.SPACE)
    el.send_keys(Keys.SPACE)
    assert el.is_selected() == False, f"{t_name} should be disable"