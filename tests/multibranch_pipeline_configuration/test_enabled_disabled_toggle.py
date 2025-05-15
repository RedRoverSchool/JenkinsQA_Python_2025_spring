from pages.new_item_page import NewItemPage

from tests.multibranch_pipeline_configuration.mbp_data import Project
from tests.multibranch_pipeline_configuration.mbp_data import Toggle


def test_default_state_of_the_toggle(new_item_page: NewItemPage):
    new_mbp_item = new_item_page.create_new_multibranch_pipeline_project(Project.PROJECT_NAME)

    assert new_mbp_item.get_state_of_the_toggle() == Toggle.TOGGLE_ENABLED_TEXT
