import pytest
from tests.freestyle_project.freestyle_data import FreestyleConfigOptTriggers

def test_trigger_section(freestyle_pj_conf_page):
    assert freestyle_pj_conf_page.check_trigger_title

@pytest.mark.parametrize("t_name", FreestyleConfigOptTriggers.TRIGGER_OPT_NAMES)
def test_each_trigger_opt_enable(freestyle_pj_conf_page, t_name):
    el = freestyle_pj_conf_page.check_box_enable(t_name)
    assert el, f"{t_name} should be enabled"

@pytest.mark.parametrize("t_name", FreestyleConfigOptTriggers.TRIGGER_OPT_NAMES)
def test_each_trigger_opt_disable(freestyle_pj_conf_page, t_name):
    el = freestyle_pj_conf_page.check_box_disable(t_name)
    assert not el, f"{t_name} should be disable"