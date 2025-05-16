from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urllib.parse import quote


class PipelinePage(BasePage):

    class Locators:
        DESCRIPTION_ELEMENT = (By.ID, "description")
        BUILD_NOW_BUTTON = (By.LINK_TEXT, "Build Now")
        BUILDS_NEXT_PAGE_BUTTON = (By.ID, "down")
        BUILDS_PREV_PAGE_BUTTON = (By.ID, "up")


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

    def create_multiple_builds(self, amount):
        for _ in range(amount):
            self.wait_to_be_clickable(self.Locators.BUILD_NOW_BUTTON).click()
        return self

    # def click_builds_next_page_button(self):
    #     import time
    #     time.sleep(5)
    #     self.click_on(self.Locators.BUILDS_NEXT_PAGE_BUTTON)
    #     return self

    # def click_builds_prev_page_button(self):
    #     self.scroll_into_view(self.Locators.BUILDS_PREV_PAGE_BUTTON)
    #     self.wait_to_be_clickable(self.Locators.BUILDS_PREV_PAGE_BUTTON, 10).click()
    #     return self
