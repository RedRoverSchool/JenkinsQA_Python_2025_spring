from urllib.parse import quote

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrganizationFolderConfigPage(BasePage):
    class Locators:
        GENERAL_BUTTON = (By.ID, "general")
        SAVE_BUTTON = (By.NAME, "Submit")

    def __init__(self, driver, name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{quote(name)}/configure"
