from urllib.parse import quote

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

import allure


class OrganizationFolderConfigPage(BasePage):
    class Locators:
        GENERAL_BUTTON = (By.ID, "general")
        SAVE_BUTTON = (By.NAME, "Submit")
        DISPLAY_NAME_FIELD = (By.NAME, "_.displayNameOrNull")

    def __init__(self, driver, name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{quote(name)}/configure"

    @allure.step('Enter Display Name: "{display_name}"')
    def add_display_name(self, display_name):
        self.enter_text(self.Locators.DISPLAY_NAME_FIELD, display_name)
        return self

    @allure.step('Click "Save" button and go to Organization Folder page: "{project_name}"')
    def click_save_button(self, project_name):
        from pages.organization_folder_page import OrganizationFolderPage
        self.wait_to_be_clickable(self.Locators.SAVE_BUTTON).click()
        return OrganizationFolderPage(self.driver, project_name).wait_for_url()
