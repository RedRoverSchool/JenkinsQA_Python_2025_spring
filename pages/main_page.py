import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class MainPage(BasePage):
    class Locators:
        NEW_ITEM_BUTTON = (By.LINK_TEXT, "New Item")
        BUILD_HISTORY_BUTTON = (By.LINK_TEXT, "Build History")
        MANAGE_JENKINS_BUTTON = (By.LINK_TEXT, "Manage Jenkins")
        TABLE_ITEM = (By.CSS_SELECTOR, "a.inside")
        BUILD_QUEUE_BLOCK = (By.ID, 'buildQueue')
        BUILD_QUEUE_HEADER = (By.CLASS_NAME, "pane-header-title")
        BUILD_QUEUE_STATUS_MESSAGE = (By.CLASS_NAME, "pane")
        BUILD_QUEUE_TOGGLE = (By.CSS_SELECTOR, "a[href = '/toggleCollapse?paneId=buildQueue']")

    JOB_NAME_LOCATOR = "//a[contains(@href, '/job/') and contains(text(), '{}')]"

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/"

    def get_item_list(self):
        return [item.text for item in self.find_elements(*self.Locators.TABLE_ITEM)]

    def go_to_new_item_page(self):
        from pages.new_item_page import NewItemPage
        self.wait_to_be_clickable(self.Locators.NEW_ITEM_BUTTON).click()
        return NewItemPage(self.driver).wait_for_url()

    def go_to_build_history_page(self):
        from pages.build_history_page import BuildHistoryPage
        self.wait_to_be_clickable(self.Locators.BUILD_HISTORY_BUTTON).click()
        return BuildHistoryPage(self.driver).wait_for_url()

    def go_to_manage_jenkins_page(self):
        from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage
        self.click_on(self.Locators.MANAGE_JENKINS_BUTTON)
        return ManageJenkinsPage(self.driver).wait_for_url()

    def go_to_folder_page(self, name):
        from pages.folder_page import FolderPage
        self.wait_to_be_clickable(self.Locators.TABLE_ITEM).click()
        return FolderPage(self.driver, name).wait_for_url()

    def wait_for_build_queue_executed(self):
        if self.wait_to_be_visible(self.Locators.BUILD_QUEUE_BLOCK).get_attribute("class").__contains__("collapsed"):
            self.wait_for_element(self.Locators.BUILD_QUEUE_TOGGLE).click()
        self.wait_text_to_be_present(self.Locators.BUILD_QUEUE_HEADER, "Build Queue (1)", 10)
        logger.info("Build Queue (1)")
        self.wait_text_to_be_present(self.Locators.BUILD_QUEUE_HEADER, "Build Queue", 10)
        logger.info("Build Queue")
        self.wait_text_to_be_present(self.Locators.BUILD_QUEUE_STATUS_MESSAGE, "No builds in the queue.", 10)
        logger.info("No builds in the queue.")
        return self

    def click_on_folder_item(self):
        self.click_on(self.Locators.TABLE_ITEM)

    def wait_for_url(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.current_url.startswith(self.url)
        )
        return self

    def is_job_with_name_displayed(self, job_name, timeout=10):
        locator = (By.XPATH, self.JOB_NAME_LOCATOR.format(job_name))
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            self.logger.warning(f"Job with name '{job_name}' not found on dashboard after {timeout} seconds.")
            return False

    def click_on_folder_by_name(self, folder_name):
        locator = (By.XPATH, f"//a[@href and text()='{folder_name}']")
        self.click_on(locator)
