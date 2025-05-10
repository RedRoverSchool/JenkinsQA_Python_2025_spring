from pages.new_item_page import NewItemPage
from tests.new_item.data import positive_name


def test_name_alphanumeric(new_item_page: NewItemPage):
    page = new_item_page
    all_validation_errors_before = page.get_any_validation_errors()
    page.enter_text_in_field(page.Locator.ITEM_NAME, positive_name)
    page.click_element(page.Locator.PAGE_NAME)
    all_validation_errors_after = page.get_any_validation_errors()

    assert len(all_validation_errors_before) == len(all_validation_errors_after), (
        "Not all validation errors were disabled before inserting any item name."
    )
    assert page.get_value(page.Locator.ITEM_NAME) == positive_name, (
        "The positive Item name did not stay in the field after clicking outside of the field."
    )
