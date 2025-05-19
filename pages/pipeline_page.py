from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urllib.parse import quote


class PipelinePage(BasePage):

    class Locator:
        DESCRIPTION_ELEMENT = (By.ID, "description")

    def __init__(self, driver, pipeline_project_name, timeout=10):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{quote(pipeline_project_name)}/"

    def is_description_element_displayed(self):
        return self.wait_for_element(self.Locator.DESCRIPTION_ELEMENT).is_displayed()

    def get_description_text(self):
        return self.wait_for_element(self.Locator.DESCRIPTION_ELEMENT).text