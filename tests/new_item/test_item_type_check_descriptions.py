from pages.new_item_page import NewItemPage
from tests.new_item.data import expected_item_descriptions


def test_display_description_of_item_type(new_item_page: NewItemPage):
    assert new_item_page.get_item_type_descriptions() == expected_item_descriptions, "Incorrect item descriptions"
    assert len(new_item_page.get_item_type_descriptions()) == len(new_item_page.get_item_type_names()), \
        "Descriptions count mismatch"
