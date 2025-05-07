from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FolderConfigPage(BasePage):
    FolderLocators = None

    class Locator:
        GENERAL_BUTTON = (By.ID, "general")
        DESCRIPTION_FIELD = (By.CSS_SELECTOR, "div.setting-main> textarea")
        PREVIEW = (By.CLASS_NAME, "textarea-show-preview")
        TEXT_PREVIEW = (By.CLASS_NAME, "textarea-preview")
        HIDE_PREVIEW = (By.CLASS_NAME, "textarea-hide-preview")

    def __init__(self, driver, folder_name,  timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{folder_name}/configure"

    def set_description(self, description):
        self.find_element(*self.Locator.DESCRIPTION_FIELD).send_keys(description)

    def click_preview(self):
        self.find_element(*self.Locator.PREVIEW).click()

    def get_preview_text(self):
        return self.wait_to_be_visible(self.Locator.TEXT_PREVIEW).text

    def hide_preview(self):
        self.find_element(*self.Locator.HIDE_PREVIEW).click()

    def get_preview_style(self):
        return self.find_element(*self.Locator.TEXT_PREVIEW).get_attribute("style")