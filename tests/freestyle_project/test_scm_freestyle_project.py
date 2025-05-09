import pytest
from tests.freestyle_project.freestyle_data import Freestyle


def test_scm_to_none(empty_configure):
    assert empty_configure

@pytest.mark.parametrize('tp_link, tp_expected_text, count', Freestyle.tooltip_scm)
def test_tooltips(freestyle, tp_link, tp_expected_text, count):
    freestyle.scroll_to_trigger()
    freestyle.click_git()
    freestyle.click_apply_button()
    freestyle.scroll_down(count)
    if 3 < count < 6:
        freestyle.click_git_advanced()
        freestyle.click_apply_button()
    assert freestyle.get_tooltip(tp_link) == tp_expected_text
