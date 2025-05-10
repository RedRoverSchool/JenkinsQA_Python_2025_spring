import pytest
from pages.freestyle_project_config_options_page import FreestylePJConfOptPage

def test_trigger_section(freestyle):
    freestyle_pj_conf_page = FreestylePJConfOptPage(freestyle)
    assert freestyle_pj_conf_page.check_trigger_title

@pytest.mark.parametrize("t_name", FreestylePJConfOptPage.TRIGGER_OPT_NAMES)
def test_each_trigger_opt_enable(freestyle, t_name):
    freestyle_pj_conf_page = FreestylePJConfOptPage(freestyle)
    el = freestyle_pj_conf_page.check_box_enable(t_name)
    assert el, f"{t_name} should be enabled"

@pytest.mark.parametrize("t_name", FreestylePJConfOptPage.TRIGGER_OPT_NAMES)
def test_each_trigger_opt_disable(freestyle, t_name):
    freestyle_pj_conf_page = FreestylePJConfOptPage(freestyle)
    el = freestyle_pj_conf_page.check_box_disable(t_name)
    assert not el, f"{t_name} should be disable"