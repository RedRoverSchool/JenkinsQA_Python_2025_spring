from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urllib.parse import quote


class PipelineConfigPage(BasePage):
    class Locators:
        GENERAL_BUTTON = (By.ID, "general")
        DESCRIPTION_FIELD = (By.NAME, 'description')
        SAVE_BUTTON = (By.NAME, "Submit")
        SCRIPT_TEXTAREA = (By.CSS_SELECTOR, "[samplesurl]>textarea")
        TEXTAREA = (By.NAME, "_.script")

    def __init__(self, driver, pipeline_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.pipeline_name = pipeline_name
        self.url = self.base_url + f"/job/{quote(pipeline_name)}/configure"

    def add_description(self, text_for_description):
        self.wait_for_element(self.Locators.DESCRIPTION_FIELD).send_keys(text_for_description)
        return self

    def click_save_button(self):
        from pages.pipeline_page import PipelinePage
        self.wait_to_be_clickable(self.Locators.SAVE_BUTTON).click()
        return PipelinePage(self.driver, pipeline_project_name=self.pipeline_name).wait_for_url()

    def type_script(self, script):
        textarea = self.wait_for_element(self.Locators.TEXTAREA)
        self.scroll_into_view(textarea)
        self.driver.execute_script("arguments[0].value = arguments[1];", textarea, script)

        return self

