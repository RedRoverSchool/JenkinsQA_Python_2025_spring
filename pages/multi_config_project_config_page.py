from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MultiConfigProjectConfigPage(BasePage):
    class Locators:
        DESCRIPTION = (By.NAME, "description")
        SUBMIT = (By.NAME, "Submit")

    def __init__(self, driver, name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{name}/configure"

    def set_description(self, text, name):
        from pages.multi_config_project_page import MultiConfigProjectPage
        self.wait_to_be_visible(self.Locators.DESCRIPTION).send_keys(text)
        self.wait_to_be_clickable(self.Locators.SUBMIT).click()
        return MultiConfigProjectPage(self.driver, name).wait_for_url()
