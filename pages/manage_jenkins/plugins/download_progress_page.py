from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DownloadProgressPage(BasePage):
    class Locator:
        TITLE_PAGE = (By.CSS_SELECTOR, "#main-panel h1")
        # LOADING_PLUGIN_EXTENSIONS = (By.)


    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/pluginManager/updates/"

    def get_title_page(self):
        return self.wait_for_element(self.Locator.TITLE_PAGE).text

