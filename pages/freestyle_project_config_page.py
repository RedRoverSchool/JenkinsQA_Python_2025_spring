from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FreestyleProjectConfigPage(BasePage):
    class Locator:
        GENERAL_BUTTON = (By.ID, "general")

    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{project_name}/configure"
