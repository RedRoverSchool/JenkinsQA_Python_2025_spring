from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AvailablePluginsPage(BasePage):
    class Locator:
        SEARCH_AVAILABLE_PLUGINS_FIELD = (By.XPATH, "//input[@placeholder='Search available plugins']")
        ITEMS_AVAILABLE_PLUGINS_LIST = (By.CSS_SELECTOR, 'tbody>tr')
        INSTALL_BUTTON = (By.XPATH, "//button[@id='button-install']")


    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/pluginManager/available"

    def is_search_available_plugins_field_visible(self):
        if self.wait_to_be_visible(self.Locator.SEARCH_AVAILABLE_PLUGINS_FIELD):
            return True
        else:
            return False

    def count_available_plugins(self):
        return len(self.wait_to_be_visible_all(self.Locator.ITEMS_AVAILABLE_PLUGINS_LIST))

    def is_install_button_visible(self):
        if self.wait_to_be_visible(self.Locator.INSTALL_BUTTON):
            return True
        else:
            return False

    def is_install_button_disabled(self):
        return self.wait_for_element(self.Locator.INSTALL_BUTTON).get_attribute("disabled")
