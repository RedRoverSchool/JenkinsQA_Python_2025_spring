from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ErrorPageCopyFrom(BasePage):
    class Locators:
        HEADER_ERROR = (By.CSS_SELECTOR, "#main-panel > h1")
        MESSAGE_ERROR = (By.CSS_SELECTOR, "#main-panel > p")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = self.base_url + "/view/all/createItem"

    def get_header_error(self):
        return self.get_visible_text(self.Locators.HEADER_ERROR)

    def get_message_error(self):
        return self.get_visible_text(self.Locators.MESSAGE_ERROR)
