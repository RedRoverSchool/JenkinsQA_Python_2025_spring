import allure
from urllib.parse import quote
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrganizationFolderPage(BasePage):
    class Locators:
        HEADER = (By.TAG_NAME, "h1")

    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{quote(project_name)}/"

    @allure.step("Get the page header text")
    def get_header_pipeline_page(self) -> str:
        return self.get_visible_text(self.Locators.HEADER)
