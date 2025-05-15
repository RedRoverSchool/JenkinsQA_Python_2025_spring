from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class JobPage(BasePage):
    class Locators:
        CREATE_A_JOB = (By.CSS_SELECTOR, 'a[href="newJob"]')
        NAME_PROJECT = (By.CSS_SELECTOR, 'td>a[href^="job/"]')
        ITEM_NAME = (By.CSS_SELECTOR, '#name')
        ITEM_PIPELINE_PROJECT = (By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob")
        OK_BUTTON = (By.CSS_SELECTOR, '#ok-button')

    def __init__(self, driver, item_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{item_name}/"

    def create_new_job(self):
        return self.click_on(self.Locators.CREATE_A_JOB)

    def item_is_present(self, item_text):
        return self.wait_text_to_be_present(self.Locators.NAME_PROJECT, item_text)

    def create_pipeline(self, item_name):
        self.wait_for_element(self.Locators.ITEM_NAME).send_keys(item_name)
        self.wait_to_be_clickable(self.Locators.ITEM_PIPELINE_PROJECT).click()
        self.wait_to_be_clickable(self.Locators.OK_BUTTON).click()
        return JobPage(self.driver, item_name)
