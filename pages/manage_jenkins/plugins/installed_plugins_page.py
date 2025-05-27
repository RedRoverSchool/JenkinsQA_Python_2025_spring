from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InstalledPluginsPage(BasePage):
    class Locator:
        SEARCH_INSTALLED_PLUGINS_FIELD = (By.XPATH, "//input[@placeholder='Search installed plugins']")
        ITEMS_INSTALLED_PLUGINS_LIST = (By.CSS_SELECTOR, 'tbody>tr')
        TABLE_BODY = (By.CSS_SELECTOR, "tbody")
        UNINSTALL_BUTTON = (By.XPATH, f"//button[@title='Uninstall SSH server']")
        CONFIRM_UNINSTALL_BUTTON = (By.XPATH, "//button[@data-id='ok']")
        UNINSTALLATION_PENDING = (By.LINK_TEXT, "Uninstallation pending")
        INSTALLED_PLUGIN = (By.XPATH, "//tr[@data-plugin-name='SSH server']")


    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + ("/manage/pluginManager/installed")

    def count_installed_plugins(self):
        return len(self.wait_to_be_visible_all(self.Locator.ITEMS_INSTALLED_PLUGINS_LIST))

    def type_plugin_name_to_search_field(self, plugin_name):
        self.enter_text(self.Locator.SEARCH_INSTALLED_PLUGINS_FIELD, plugin_name)
        count = 50
        while count > 5:
            count = len(self.wait_for_element(self.Locator.TABLE_BODY).text.split("\n"))
        return self

    def click_uninstall(self):
        self.wait_for_element(self.Locator.UNINSTALL_BUTTON).click()
        self.wait_to_be_clickable(self.Locator.CONFIRM_UNINSTALL_BUTTON).click()
        count = 1
        while count < 2:
            count = self.count_installed_plugins()
        return self

    def is_plugin_installed(self, plugin_name):
        return self.wait_text_to_be_present(self.Locator.INSTALLED_PLUGIN, plugin_name)
