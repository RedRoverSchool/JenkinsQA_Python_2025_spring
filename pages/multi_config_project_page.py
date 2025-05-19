from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MultiConfigProjectPage(BasePage):
    class Locators:
        SAVED_DESCRIPTION = (By.CSS_SELECTOR, "#description>div:first-child")
        EDIT_LINK = (By.ID, "description-link")
        DESCRIPTION_INPUT = (By.NAME, "description")
        SUBMIT = (By.NAME, "Submit")

    def __init__(self, driver, name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{name}/"

    def get_saved_description_text(self):
        return self.wait_to_be_visible(self.Locators.SAVED_DESCRIPTION).text

    def edit_description(self, new_text):
        self.click_on(self.Locators.EDIT_LINK)
        input_field = self.wait_to_be_visible(self.Locators.DESCRIPTION_INPUT)
        input_field.clear()
        input_field.send_keys(new_text)
        self.click_on(self.Locators.SUBMIT)
        return self.wait_for_url()
