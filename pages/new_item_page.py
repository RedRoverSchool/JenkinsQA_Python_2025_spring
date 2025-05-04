from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NewItemPage(BasePage):
    class Locator:
        ITEM_NAME = (By.CSS_SELECTOR, '#name')
        ITEM_FOLDER = (By.CSS_SELECTOR, '[class*="cloudbees_hudson_plugins_folder"]')
        ITEM_FREESTYLE_PROJECT = (By.CSS_SELECTOR, '[class*="hudson_model_FreeStyleProject"]')
        OK_BUTTON = (By.CSS_SELECTOR, '#ok-button')

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/view/all/newJob"

    def create_new_folder(self, name):
        from pages.folder_config_page import FolderConfigPage
        self.wait_for_element(self.Locator.ITEM_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locator.ITEM_FOLDER).click()
        self.wait_to_be_clickable(self.Locator.OK_BUTTON).click()
        return FolderConfigPage(self.driver, name).wait_for_url()

    def create_new_freestyle_project(self, name):
        from pages.freestyle_project_config_page import FreestyleProjectConfigPage
        self.wait_for_element(self.Locator.ITEM_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locator.ITEM_FREESTYLE_PROJECT).click()
        self.wait_to_be_clickable(self.Locator.OK_BUTTON).click()
        return FreestyleProjectConfigPage(self.driver, name).wait_for_url()
