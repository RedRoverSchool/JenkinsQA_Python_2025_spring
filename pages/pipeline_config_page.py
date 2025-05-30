from urllib.parse import quote

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PipelineConfigPage(BasePage):
    class Locators:
        GENERAL_BUTTON = (By.ID, "general")
        DESCRIPTION_FIELD = (By.NAME, 'description')
        SAVE_BUTTON = (By.NAME, "Submit")
        TITLE_TRIGGERS = (By.ID, "triggers")
        DESCRIPTION_TRIGGERS = (By.CSS_SELECTOR, "#triggers + .jenkins-section__description")

    def __init__(self, driver, pipeline_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.pipeline_name = pipeline_name
        self.url = self.base_url + f"/job/{quote(pipeline_name)}/configure"

    def wait_for_page(self):
        return self.wait_for_element(self.Locators.GENERAL_BUTTON)

    def add_description(self, text_for_description):
        self.wait_for_element(self.Locators.DESCRIPTION_FIELD).send_keys(text_for_description)
        return self

    def click_save_button(self, pipeline_project_name):
        from pages.pipeline_page import PipelinePage
        self.wait_to_be_clickable(self.Locators.SAVE_BUTTON).click()
        return PipelinePage(self.driver, pipeline_project_name).wait_for_url()

    def get_title_triggers(self):
        return self.get_visible_text(self.Locators.TITLE_TRIGGERS)

    def get_description_triggers(self):
        return self.get_visible_text(self.Locators.DESCRIPTION_TRIGGERS)
