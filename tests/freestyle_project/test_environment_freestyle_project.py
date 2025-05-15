import pytest
from tests.freestyle_project.freestyle_data import Freestyle

def test_exist_environment_section(freestyle):
    assert freestyle.get_environment_element().is_displayed()

@pytest.mark.parametrize('tp_link, tp_expected_text', Freestyle.tooltip_environment)
def test_tooltip_environment_items(freestyle, tp_link, tp_expected_text):
    freestyle.scroll_to_post_build_actions()
    tp_text = freestyle.get_tooltip(tp_link)
    assert tp_text == tp_expected_text

def test_create_freestyle_without_environment(freestyle):
    freestyle_page = freestyle.click_save_button()
    assert freestyle_page.get_title() == f"{Freestyle.project_name} [Jenkins]"
