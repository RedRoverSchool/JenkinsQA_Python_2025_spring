from pages.new_item_page import NewItemPage
from tests.new_item.data import new_freestyle_project_name


def test_create_freestyle_project(new_item_page: NewItemPage):
    items = new_item_page.create_new_freestyle_project(new_freestyle_project_name).go_to_the_main_page().get_item_list()

    assert len(items) == 1, f"Expected 1, but {len(items)} projects were created"
    assert items[0] == new_freestyle_project_name, f"Freestyle project '{new_freestyle_project_name}' NOT FOUND"
