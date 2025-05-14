from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urllib.parse import quote


class PipelinePage(BasePage):

    class Locators:
        DESCRIPTION_ELEMENT = (By.ID, "description")
        BUILD_NOW_BUTTON = (By.LINK_TEXT, "Build Now")

    def __init__(self, driver, pipeline_project_name, timeout=10):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{quote(pipeline_project_name)}/"

    def is_description_element_displayed(self):
        return self.wait_for_element(self.Locators.DESCRIPTION_ELEMENT).is_displayed()

    def get_description_text(self):
        return self.wait_for_element(self.Locators.DESCRIPTION_ELEMENT).text

    def click_build_now_button(self):
        self.wait_to_be_clickable(self.Locators.BUILD_NOW_BUTTON).click()
        return self