import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from tests.multibranch_pipeline_configuration.mbp_data import Toggle
class MultibranchPipelineConfigPage(BasePage):
    class Locators:
        PROPERTIES_SECTION = (By.ID, "properties")
        BRANCH_SOURCES_SECTION = (By.ID, "branch-sources")

    def __init__(self, driver, job_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{job_name}/configure"

    def get_state_of_the_toggle(self):
        return self.find_element(*Toggle.TOGGLE).text

    @allure.step("Get Properties section element")
    def get_properties_section(self):
        properties_section = self.wait_to_be_visible(self.Locators.PROPERTIES_SECTION)
        self.scroll_into_view(properties_section)
        return properties_section

    @allure.step("Get Branch Sources section element")
    def get_branch_sources_section(self):
        branch_sources_section = self.wait_to_be_visible(self.Locators.BRANCH_SOURCES_SECTION)
        self.scroll_into_view(branch_sources_section)
        return branch_sources_section