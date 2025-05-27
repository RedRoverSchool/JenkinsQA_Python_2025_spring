from pages.manage_jenkins.plugins.plugins_page import PluginsPage
from selenium.webdriver.common.by import By


class DownloadProgressPage(PluginsPage):
    class Locator:
        TITLE_PAGE = (By.CSS_SELECTOR, "#main-panel h1")
        LOADING_PLUGIN_EXTENSIONS_STATUS = (By.XPATH, "//tbody/tr[3]/td[@id='status14']")
        PLUGIN_NAME_STATUS = (By.XPATH, "//tbody/tr[2]/td[@id='status12']")
        INSTALLED_PLUGINS = (By.LINK_TEXT, "Installed plugins")


    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/pluginManager/updates/"

    def get_title_page(self):
        return self.wait_for_element(self.Locator.TITLE_PAGE).text

    def is_success_loading_plugin_extensions(self):
        return self.wait_text_to_be_present(self.Locator.LOADING_PLUGIN_EXTENSIONS_STATUS, "Success", 10)

    def is_success_plugin_name(self):
        return self.wait_text_to_be_present(self.Locator.PLUGIN_NAME_STATUS, "Success", 10)
