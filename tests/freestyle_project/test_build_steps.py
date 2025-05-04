from pages.new_item_page import NewItemPage
from tests.new_item.data import new_freestyle_project_name, build_steps_list


def test_build_steps_availability(new_item_page: NewItemPage):
    freestyle_project_config_page = new_item_page.create_new_freestyle_project(
        new_freestyle_project_name
    )
    build_steps_we = freestyle_project_config_page.get_build_steps_list()
    build_steps_items = {el.text for el in build_steps_we}

    assert build_steps_list == build_steps_items
