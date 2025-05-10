from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MultiConfigProjectPage(BasePage):
    class Locators:
        SAVED_DESCRIPTION = (By.CSS_SELECTOR, "#description>div:first-child")

    def __init__(self, driver, name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{name}/"

    def get_saved_description_text(self):
        return self.wait_to_be_visible(self.Locators.SAVED_DESCRIPTION).text
