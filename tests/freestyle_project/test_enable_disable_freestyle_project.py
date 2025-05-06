from tests.freestyle_project.freestyle_data import Freestyle


def test_enable_disable_switch(freestyle):
    assert freestyle.is_enable().is_displayed()
    freestyle.switch_to_disable()
    assert freestyle.is_disable().is_displayed()

def test_tooltip(tooltip):
    assert tooltip == Freestyle.tooltip_disable

def test_disabled_message(disabled_message):
    assert disabled_message == Freestyle.warning_message

def test_enable_after_disabled(enable_automatically):
    assert enable_automatically[0] and enable_automatically[1]
