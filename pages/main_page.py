import logging
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class MainPage(BasePage):
    class Locator:
        NEW_ITEM_BUTTON = (By.LINK_TEXT, "New Item")
        BUILD_HISTORY_BUTTON = (By.LINK_TEXT, "Build History")
        MANAGE_JENKINS_BUTTON = (By.LINK_TEXT, "Manage Jenkins")
        TABLE_ITEM = (By.CSS_SELECTOR, "a.inside")
        BUILD_QUEUE_BLOCK = (By.ID, 'buildQueue')
        BUILD_QUEUE_HEADER = (By.CLASS_NAME, "pane-header-title")
        BUILD_QUEUE_STATUS_MESSAGE = (By.CLASS_NAME, "pane")
        BUILD_QUEUE_TOGGLE = (By.CSS_SELECTOR, "a[href = '/toggleCollapse?paneId=buildQueue']")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/"

    def get_item_list(self):
        return [item.text for item in self.find_elements(*self.Locator.TABLE_ITEM)]

    def go_to_new_item_page(self):
        from pages.new_item_page import NewItemPage
        self.wait_to_be_clickable(self.Locator.NEW_ITEM_BUTTON).click()
        return NewItemPage(self.driver).wait_for_url()

    def go_to_build_history_page(self):
        from pages.build_history_page import BuildHistoryPage
        self.wait_to_be_clickable(self.Locator.BUILD_HISTORY_BUTTON).click()
        return BuildHistoryPage(self.driver).wait_for_url()

    def go_to_manage_jenkins_page(self):
        from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage
        self.click_on(self.Locator.MANAGE_JENKINS_BUTTON)
        return ManageJenkinsPage(self.driver).wait_for_url()

    def wait_for_build_queue_executed(self):
        if self.wait_to_be_visible(self.Locator.BUILD_QUEUE_BLOCK).get_attribute("class").__contains__("collapsed"):
            self.wait_for_element(self.Locator.BUILD_QUEUE_TOGGLE).click()
        self.wait_text_to_be_present(self.Locator.BUILD_QUEUE_HEADER, "Build Queue (1)", 10)
        logger.info("Build Queue (1)")
        self.wait_text_to_be_present(self.Locator.BUILD_QUEUE_STATUS_MESSAGE, "No builds in the queue.", 10)
        logger.info("No builds in the queue.")
        return self
