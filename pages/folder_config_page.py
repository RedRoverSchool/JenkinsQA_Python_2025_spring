from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.folder_page import FolderPage


class FolderConfigPage(BasePage):
    class Locators:
        GENERAL_BUTTON = (By.ID, "general")
        SAVE_BUTTON = (By.CSS_SELECTOR, "[name='Submit']")
        DESCRIPTION = (By.XPATH, "//*[@id='view-message']")
        DESCRIPTION_FIELD = (By.CSS_SELECTOR, "div.setting-main> textarea")
        PREVIEW = (By.CLASS_NAME, "textarea-show-preview")
        TEXT_PREVIEW = (By.CLASS_NAME, "textarea-preview")
        HIDE_PREVIEW = (By.CLASS_NAME, "textarea-hide-preview")
        HEALTH_METRICS = (By.ID, "health-metrics")
        FOLDER_NAME = (By.CSS_SELECTOR, "#main-panel> h1")

    def __init__(self, driver, folder_name,  timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{folder_name}/configure"
        self.name = folder_name

    def set_description(self, description):
        self.find_element(*self.Locators.DESCRIPTION_FIELD).send_keys(description)

    def click_preview(self):
        self.find_element(*self.Locators.PREVIEW).click()

    def get_preview_text(self):
        return self.wait_to_be_visible(self.Locators.TEXT_PREVIEW).text

    def hide_preview(self):
        self.find_element(*self.Locators.HIDE_PREVIEW).click()

    def get_preview_style(self):
        return self.find_element(*self.Locators.TEXT_PREVIEW).get_attribute("style")

    def has_health_metrics_text(self):
        element = self.find_element(*self.Locators.HEALTH_METRICS)
        return element is not None and "Health metrics" in element.text

    def is_health_metrics_clickable(self):
        element = self.find_element(*self.Locators.HEALTH_METRICS)
        return element is not None and element.is_displayed() and element.is_enabled()

    def click_save_button(self):
        self.click_on(self.Locators.SAVE_BUTTON)
        return FolderPage(self.driver, folder_name = self.name).wait_for_url()

    def get_folder_name_after_click_save(self):
        name = self.wait_to_be_visible(self.Locators.FOLDER_NAME).text
        return name