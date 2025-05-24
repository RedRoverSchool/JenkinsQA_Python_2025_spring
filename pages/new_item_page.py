import time
from typing import List
import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class NewItemPage(BasePage):
    class Locators:
        PAGE_NAME = (By.XPATH, "//h1[text()='New Item']")
        ITEM_NAME = (By.CSS_SELECTOR, '#name')
        ITEM_FOLDER = (By.CSS_SELECTOR, '[class*="cloudbees_hudson_plugins_folder"]')
        OK_BUTTON = (By.CSS_SELECTOR, '#ok-button')

        ITEM_PIPELINE_PROJECT = (By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob")
        ITEM_FREESTYLE_PROJECT = (By.CLASS_NAME, "hudson_model_FreeStyleProject")
        ITEM_MULTIBRANCH_PIPELINE_PROJECT = (
            By.CLASS_NAME, "org_jenkinsci_plugins_workflow_multibranch_WorkflowMultiBranchProject"
        )

        SELECTED_ITEM = (By.XPATH, "//li[@aria-checked='true']")
        ACTIVE_ITEM = (By.CLASS_NAME, "active")

        ERROR_MESSAGE = (By.ID, "itemname-required")
        ANY_ENABLED_ERROR = (By.CSS_SELECTOR, ".input-validation-message:not(.input-message-disabled)")

        ITEM_MULTI_CONFIG_PROJECT = (By.CLASS_NAME, "hudson_matrix_MatrixProject")
        ITEM_TYPES = (By.CSS_SELECTOR, ".label")
        ITEM_DESCRIPTIONS = (By.XPATH, "//div[@class='desc']")
        COPY_FROM = (By.ID, "from")
        DROPDOWN_COPY = (By.CSS_SELECTOR, "div.jenkins-dropdown")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/view/all/newJob"

    def wait_for_page(self):
        return self.wait_for_element(self.Locators.PAGE_NAME)

    @allure.step("Create new folder: \"{name}\"")
    def create_new_folder(self, name):
        from pages.folder_config_page import FolderConfigPage
        self.wait_for_element(self.Locators.ITEM_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locators.ITEM_FOLDER).click()
        self.wait_to_be_clickable(self.Locators.OK_BUTTON).click()
        return FolderConfigPage(self.driver, name).wait_for_url()

    @allure.step("Create new freestyle project: \"{name}\"")
    def create_new_freestyle_project(self, name):
        from pages.freestyle_project_config_page import FreestyleProjectConfigPage
        with allure.step("Input project name \"{name}\""):
            self.wait_for_element(self.Locators.ITEM_NAME).send_keys(name)
        with allure.step("Select \"Freestyle project\" type"):
            self.wait_to_be_clickable(self.Locators.ITEM_FREESTYLE_PROJECT).click()
        with allure.step("Click \"OK\" button"):
            self.wait_to_be_clickable(self.Locators.OK_BUTTON).click()
        return FreestyleProjectConfigPage(self.driver, name).wait_for_url()

    def create_new_pipeline_project(self, name):
        from pages.pipeline_config_page import PipelineConfigPage
        self.wait_for_element(self.Locators.ITEM_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locators.ITEM_PIPELINE_PROJECT).click()
        self.wait_to_be_clickable(self.Locators.OK_BUTTON).click()
        return PipelineConfigPage(self.driver, name).wait_for_url()

    def create_new_multibranch_pipeline_project(self, name):
        from pages.multibranch_pipeline_config_page import MultibranchPipelineConfigPage
        self.wait_for_element(self.Locators.ITEM_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locators.ITEM_MULTIBRANCH_PIPELINE_PROJECT).click()
        self.wait_to_be_clickable(self.Locators.OK_BUTTON).click()
        return MultibranchPipelineConfigPage(self.driver, name)

    def get_pipeline_element(self):
        return self.find_element(*self.Locators.ITEM_PIPELINE_PROJECT)

    def get_freestyle_element(self):
        return self.find_element(*self.Locators.ITEM_FREESTYLE_PROJECT)

    def click_ok_button(self):
        return self.click_on(self.Locators.OK_BUTTON)

    def click_element(self, element):
        self.wait_to_be_clickable(element).click()

    def get_active_element(self):
        return self.wait_for_element(self.Locators.ACTIVE_ITEM)

    def get_selected_items(self):
        return self.find_elements(*self.Locators.SELECTED_ITEM)

    def get_highlighted_items(self):
        return self.find_elements(*self.Locators.ACTIVE_ITEM)

    def get_error_message(self):
        self.wait_for_element(self.Locators.OK_BUTTON).click()
        return self.wait_for_element(self.Locators.ERROR_MESSAGE).text.strip()

    def get_any_validation_errors(self) -> List[WebElement]:
        time.sleep(1)  # sleep is needed for cases when errors should not appear
        return self.find_elements(
            *self.Locators.ANY_ENABLED_ERROR
        )

    @allure.step("Create new Multi-configuration project: \"{name}\"")
    def create_new_multi_config_project(self, name):
        from pages.multi_config_project_config_page import MultiConfigProjectConfigPage
        self.wait_for_element(self.Locators.ITEM_NAME).send_keys(name)
        item_multi_config_project = self.wait_to_be_clickable(self.Locators.ITEM_MULTI_CONFIG_PROJECT)
        self.scroll_into_view(item_multi_config_project)
        item_multi_config_project.click()
        self.wait_to_be_clickable(self.Locators.OK_BUTTON).click()
        return MultiConfigProjectConfigPage(self.driver, name).wait_for_url()

    def get_item_type_names(self):
        elements = self.wait_to_be_visible_all(self.Locators.ITEM_TYPES)
        return [element.text for element in elements]

    def copy_from_option_is_displayed(self):
        return self.wait_to_be_visible(self.Locators.COPY_FROM).is_displayed()

    def get_item_type_descriptions(self):
        return [desc.text.strip() for desc in self.find_elements(*self.Locators.ITEM_DESCRIPTIONS)]

    @allure.step("Create new Pipeline project: \"{name}\"")
    def create_new_pipeline(self, name):
        from pages.pipeline_config_page import PipelineConfigPage
        self.wait_for_element(self.Locators.ITEM_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locators.ITEM_PIPELINE_PROJECT).click()
        self.wait_to_be_clickable(self.Locators.OK_BUTTON).click()
        return PipelineConfigPage(self.driver, name).wait_for_url()

    def get_dropdown_text(self):
        try:
            return self.get_visible_text_lines(self.Locators.DROPDOWN_COPY)
        except TimeoutException:
            self.logger.error("Dropdown did not appear: element is not visible on the page.")
            return []

    def enter_item_name(self, name):
        self.enter_text(self.Locators.ITEM_NAME, name)
        return self

    def enter_copy_from(self, name):
        self.enter_text(self.Locators.COPY_FROM, name)
        return self

    def enter_first_character_in_copy_from(self, name):
        self.enter_copy_from(name[0])
        return self

    def go_to_error_page_copy(self, name, copy_name):
        from pages.error_page_copy_from import ErrorPageCopyFrom
        self.enter_item_name(name).enter_copy_from(copy_name).click_ok_button()
        return ErrorPageCopyFrom(self.driver).wait_for_url()

    def select_item_from_dropdown(self):
        return self.click_on(self.Locators.DROPDOWN_COPY)

    def get_copy_from_field_value(self):
        return self.get_attribute(self.Locators.COPY_FROM, "value")
