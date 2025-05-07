from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class NewItemPage(BasePage):
    class Locator:
        ITEM_NAME = (By.CSS_SELECTOR, '#name')
        ITEM_FOLDER = (By.CSS_SELECTOR, '[class*="cloudbees_hudson_plugins_folder"]')
        OK_BUTTON = (By.CSS_SELECTOR, '#ok-button')
        ITEM_PIPELINE_PROJECT = (By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob")
        ITEM_FREESTYLE_PROJECT = (By.CLASS_NAME, "hudson_model_FreeStyleProject")
        SELECTED_ITEM = (By.XPATH, "//li[@aria-checked='true']")
        ACTIVE_ITEM = (By.CLASS_NAME, "active")
        ERROR_MESSAGE = (By.ID, "itemname-required")
        ITEM_MULTI_CONFIG_PROJECT = (By.CLASS_NAME, "hudson_matrix_MatrixProject")
        ITEM_TYPES = (By.CSS_SELECTOR, ".label")
        ITEM_DESCRIPTIONS = (By.XPATH, "//div[@class='desc']")
        COPY_FROM = (By.ID, "from")
        DROPDOWN_COPY = (By.CSS_SELECTOR, "div.jenkins-dropdown")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/view/all/newJob"

    def create_new_folder(self, name):
        from pages.folder_config_page import FolderConfigPage
        self.wait_for_element(self.Locator.ITEM_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locator.ITEM_FOLDER).click()
        self.wait_to_be_clickable(self.Locator.OK_BUTTON).click()
        return FolderConfigPage(self.driver, name).wait_for_url()

    def create_new_freestyle_project(self, name):
        from pages.freestyle_project_config_page import FreestyleProjectConfigPage
        self.wait_for_element(self.Locator.ITEM_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locator.ITEM_FREESTYLE_PROJECT).click()
        self.wait_to_be_clickable(self.Locator.OK_BUTTON).click()
        return FreestyleProjectConfigPage(self.driver, name).wait_for_url()

    def get_pipeline_element(self):
        return self.find_element(*self.Locator.ITEM_PIPELINE_PROJECT)

    def get_freestyle_element(self):
        return self.find_element(*self.Locator.ITEM_FREESTYLE_PROJECT)

    def click_element(self, element):
        self.wait_to_be_clickable(element).click()

    def get_active_element(self):
        return self.wait_for_element(self.Locator.ACTIVE_ITEM)

    def get_selected_items(self):
        return self.find_elements(*self.Locator.SELECTED_ITEM)

    def get_highlighted_items(self):
        return self.find_elements(*self.Locator.ACTIVE_ITEM)

    def get_error_message(self):
        self.wait_for_element(self.Locator.OK_BUTTON).click()
        return self.wait_for_element(self.Locator.ERROR_MESSAGE).text.strip()

    def create_new_multi_config_project(self, name):
        from pages.multi_config_project_config_page import MultiConfigProjectConfigPage
        self.wait_for_element(self.Locator.ITEM_NAME).send_keys(name)
        item_multi_config_project = self.wait_to_be_clickable(self.Locator.ITEM_MULTI_CONFIG_PROJECT)
        self.scroll_into_view(item_multi_config_project)
        item_multi_config_project.click()
        self.wait_to_be_clickable(self.Locator.OK_BUTTON).click()
        return MultiConfigProjectConfigPage(self.driver, name).wait_for_url()

    def get_item_type_names(self):
        elements = self.wait_to_be_visible_all(self.Locator.ITEM_TYPES)
        return [element.text for element in elements]

    def get_item_type_descriptions(self):
        return [desc.text.strip() for desc in self.find_elements(*self.Locator.ITEM_DESCRIPTIONS)]

    def get_dropdown_text(self):
        try:
            return self.wait_to_be_visible(self.Locator.DROPDOWN_COPY).text.splitlines()
        except TimeoutException:
            self.logger.error("Dropdown did not open and is not present in the DOM.")
            return []

    def create_folder_and_open_page(self, name):
        self.create_new_folder(name)
        return self.go_to_the_main_page().go_to_new_item_page()

    def enter_first_letter_in_copy_from(self, name):
        self.enter_text_in_field(self.Locator.COPY_FROM, name[0])
        return self
