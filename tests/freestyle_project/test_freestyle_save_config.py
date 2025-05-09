from tests.freestyle_project.freestyle_data import Freestyle


def test_buttons_available(freestyle):
    assert freestyle.is_save_button_available() and freestyle.is_apply_button_available()

def test_save_config(freestyle):
    project_page = freestyle.click_save_button()
    assert project_page.get_h1_value() == Freestyle.project_name

def test_applay_config(freestyle):
    freestyle.click_apply_button()
    assert freestyle.is_notification_was_visible()
    assert freestyle.get_h1_text() == 'Configure'
