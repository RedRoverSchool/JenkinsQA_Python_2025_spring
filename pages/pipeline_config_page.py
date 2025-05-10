from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PipelineConfigPage(BasePage):
    class Locators:
        GENERAL_BUTTON = (By.ID, "general")

    def __init__(self, driver, pipeline_name,  timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{pipeline_name}/configure"