from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FolderPage(BasePage):
    class Locator:
       EMPTY_STATE_MESSAGE = (By.XPATH, "//h2")

    def __init__(self, driver, folder_name,  timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{folder_name}/"

    def get_empty_state_message(self):
        return self.wait_to_be_visible(self.Locator.EMPTY_STATE_MESSAGE).text