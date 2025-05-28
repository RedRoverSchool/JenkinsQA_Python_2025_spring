from pages.manage_jenkins.plugins.plugins_page import PluginsPage
from selenium.webdriver.common.by import By


class AvailablePluginsPage(PluginsPage):
    class Locator:
        SEARCH_AVAILABLE_PLUGINS_FIELD = (By.XPATH, "//input[@placeholder='Search available plugins']")
        ITEMS_AVAILABLE_PLUGINS_LIST = (By.CSS_SELECTOR, 'tbody>tr')
        INSTALL_BUTTON = (By.XPATH, "//button[@id='button-install']")
        TABLE_BODY = (By.CSS_SELECTOR, "tbody")
        CHECKBOX_PLUGIN = (By.CSS_SELECTOR, "tbody>tr span[class='jenkins-checkbox']")
        INSTALLED_PLUGINS = (By.LINK_TEXT, "Installed plugins")


    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/pluginManager/available"

    def is_search_available_plugins_field_visible(self):
        if self.wait_to_be_visible(self.Locator.SEARCH_AVAILABLE_PLUGINS_FIELD):
            return True
        else:
            return False

    def count_available_plugins(self):
        if len(self.wait_for_element(self.Locator.TABLE_BODY).text.split("\n")) > 1:
            return len(self.wait_to_be_visible_all(self.Locator.ITEMS_AVAILABLE_PLUGINS_LIST))
        else:
            return 0

    def is_install_button_visible(self):
        if self.wait_to_be_visible(self.Locator.INSTALL_BUTTON):
            return True
        else:
            return False

    def is_install_button_disabled(self):
        return self.wait_for_element(self.Locator.INSTALL_BUTTON).get_attribute("disabled")

    def type_plugin_name_to_search_field(self, plugin_name):
        self.enter_text(self.Locator.SEARCH_AVAILABLE_PLUGINS_FIELD, plugin_name)
        count = 50
        while count > 5:
            count = len(self.wait_for_element(self.Locator.TABLE_BODY).text.split("\n"))
        return self

    def select_plugin_checkbox(self):
        self.wait_for_element(self.Locator.CHECKBOX_PLUGIN).click()
        return self

    def click_install_button(self):
        from pages.manage_jenkins.plugins.download_progress_page import DownloadProgressPage
        self.click_on(self.Locator.INSTALL_BUTTON)
        return DownloadProgressPage(self.driver)
