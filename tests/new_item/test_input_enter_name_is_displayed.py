from .data_structs import NewItem


def test_name_input_is_displayed(new_item_page):
    name_input = new_item_page.find_element(*NewItem.name_field_selector)

    assert name_input.is_displayed()
