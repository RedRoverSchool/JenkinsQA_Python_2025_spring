import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PluginsPage(BasePage):
    class Locator:
        AVAILABLE_PLUGINS = (By.LINK_TEXT, "Available plugins")
        INSTALLED_PLUGINS = (By.LINK_TEXT, "Installed plugins")


    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/pluginManager/"

    @allure.step("Go to Available Plugins Page")
    def go_to_available_plugins_page(self):
        from pages.manage_jenkins.plugins.available_plugins_page import AvailablePluginsPage
        self.click_on(self.Locator.AVAILABLE_PLUGINS)
        return AvailablePluginsPage(self.driver).wait_for_url()

    def go_to_installed_plugins_page(self):
        from pages.manage_jenkins.plugins.installed_plugins_page import InstalledPluginsPage
        self.click_on(self.Locator.INSTALLED_PLUGINS)
        return InstalledPluginsPage(self.driver).wait_for_url()

    def is_available_plugins_displayed(self):
        if self.wait_to_be_clickable(self.Locator.AVAILABLE_PLUGINS):
            return True
        else:
            return False