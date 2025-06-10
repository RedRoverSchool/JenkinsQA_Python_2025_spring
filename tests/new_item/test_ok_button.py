from pages.new_item_page import NewItemPage


def test_ok_button_disabled(new_item_page: NewItemPage):
    new_item_page.scroll_to_element(*new_item_page.Locators.OK_BUTTON)
    is_disabled = new_item_page.find_element(*new_item_page.Locators.OK_BUTTON).get_attribute("disabled")

    assert is_disabled, f"Ok button is not disabled by default on the {new_item_page.__class__.__name__}"
