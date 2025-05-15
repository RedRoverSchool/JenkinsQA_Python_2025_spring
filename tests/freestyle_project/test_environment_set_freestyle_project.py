import pytest
from tests.freestyle_project.freestyle_data import Freestyle


@pytest.mark.parametrize('item_name, id_check', Freestyle.environmet_options)
def test_possible_set_environment(freestyle, item_name, id_check):
    freestyle.scroll_to_post_build_actions()
    freestyle.click_on_checkbox_environment_options(item_name)
    freestyle.click_apply_button()
    assert freestyle.is_checkbox_environment_options_selected(id_check)