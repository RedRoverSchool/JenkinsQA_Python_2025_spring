import logging


class NewItem:
    url = "/view/all/newJob"
    new_item_button_selector = "a[href='/view/all/newJob']"
    name_field_selector = "#name"
    positive_name = "nameForTestCase_01.001.04"
    page_name_selector = "//h1[text()='New Item']"
    common_validation_error_selector = ".input-message-disabled"

    @classmethod
    def assert_message(cls, message=""):
        logging.info(f"Assertion error detected on New Item page.{message}'")
