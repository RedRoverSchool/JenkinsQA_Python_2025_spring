from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MultiConfigProjectConfigPage(BasePage):
    class Locator:
        DESCRIPTION = (By.NAME, "description")
        SUBMIT = (By.NAME, "Submit")
        SAVED_DESCRIPTION = (By.ID, "description")

    def set_description(self, text):
        self.wait_to_be_visible(self.Locator.DESCRIPTION).send_keys(text)
        self.click_on(self.Locator.SUBMIT)

    def get_saved_description_text(self):
        return self.wait_to_be_visible(self.Locator.SAVED_DESCRIPTION).text
