from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PipelineConfigPage(BasePage):
    class Locators:
        GENERAL_BUTTON = (By.ID, "general")
        DESCRIPTION_FIELD = (By.NAME, 'description')
        SAVE_BUTTON = (By.NAME, "Submit")

    def __init__(self, driver, *pipeline_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.pipeline_parts = self.normalize_path_parts(*pipeline_name)
        self.url = f"{self.base_url}/{self.build_path(*self.pipeline_parts)}/configure"

    def add_description(self, text_for_description):
        self.wait_for_element(self.Locators.DESCRIPTION_FIELD).send_keys(text_for_description)
        return self

    def click_save_button(self, pipeline_project_name):
        from pages.pipeline_page import PipelinePage
        self.wait_to_be_clickable(self.Locators.SAVE_BUTTON).click()
        return PipelinePage(self.driver, *self.pipeline_parts, pipeline_project_name).wait_for_url()
