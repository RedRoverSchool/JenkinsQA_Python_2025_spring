import logging
from urllib.parse import quote

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.ui_element import UIElementMixin
from pages.folder_page import FolderPage

logger = logging.getLogger(__name__)


class MainPage(BasePage, UIElementMixin):
    class Locators:
        PAGE_NAME = (By.XPATH, "//a[text()='Dashboard']")
        NEW_ITEM_BUTTON = (By.LINK_TEXT, "New Item")
        BUILD_HISTORY_BUTTON = (By.LINK_TEXT, "Build History")
        MANAGE_JENKINS_BUTTON = (By.LINK_TEXT, "Manage Jenkins")
        TABLE_ITEM = (By.CSS_SELECTOR, "a.inside")
        BUILD_QUEUE_BLOCK = (By.ID, 'buildQueue')
        BUILD_QUEUE_HEADER = (By.CLASS_NAME, "pane-header-title")
        BUILD_QUEUE_STATUS_MESSAGE = (By.CLASS_NAME, "pane")
        BUILD_QUEUE_TOGGLE = (By.CSS_SELECTOR, "a[href = '/toggleCollapse?paneId=buildQueue']")
        FOLDER_LINK_LOCATOR = "//*[@id='job_{}']/td[3]/a"

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/"

    def get_table_item_locator(self, name: str):
        return (By.LINK_TEXT, quote(name))

    @allure.step("Get list of items from \"Dashboard\"")
    def get_item_list(self):
        return [item.text for item in self.find_elements(*self.Locators.TABLE_ITEM)]

    def go_to_new_item_page(self):
        from pages.new_item_page import NewItemPage
        return self.navigate_to(NewItemPage, self.Locators.NEW_ITEM_BUTTON)

    def go_to_build_history_page(self):
        from pages.build_history_page import BuildHistoryPage
        self.wait_to_be_clickable(self.Locators.BUILD_HISTORY_BUTTON).click()
        return BuildHistoryPage(self.driver).wait_for_url()

    def go_to_manage_jenkins_page(self):
        from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage
        self.click_on(self.Locators.MANAGE_JENKINS_BUTTON)
        return ManageJenkinsPage(self.driver).wait_for_url()

    @allure.step("Go to the folder page: \"{name}\"")
    def go_to_the_folder_page(self, name):
        from pages.folder_page import FolderPage
        return self.navigate_to(FolderPage, self.get_table_item_locator(name), name)

    def show_build_queue_info_block(self):
        if self.wait_to_be_visible(self.Locators.BUILD_QUEUE_BLOCK).get_attribute("class").__contains__("collapsed"):
            self.wait_for_element(self.Locators.BUILD_QUEUE_TOGGLE).click()

    def wait_for_build_queue_executed(self):
        self.show_build_queue_info_block()
        logger.info("Getting message 'Build Queue (1)'")
        self.wait_text_to_be_present(self.Locators.BUILD_QUEUE_HEADER, "Build Queue (1)", 10)
        logger.info("Getting message 'Build Queue'")
        self.wait_text_to_be_present(self.Locators.BUILD_QUEUE_HEADER, "Build Queue", 10)
        logger.info("Getting message 'No builds in the queue.'")
        self.wait_text_to_be_present(self.Locators.BUILD_QUEUE_STATUS_MESSAGE, "No builds in the queue.", 10)
        return self

    def open_dashboard_in_new_window(self):
        self.driver.execute_script(f"window.open('{self.url}');")
        self.wait_for_new_window()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return MainPage(self.driver)

    @allure.step("Click on folder by name")
    def click_on_folder_by_name(self, folder_name, timeout=10):
        locator = (By.XPATH, self.Locators.FOLDER_LINK_LOCATOR.format(folder_name))
        self.logger.info(f"Clicking on folder with locator: {locator}")
        self.click_on(locator, timeout=timeout)
        return FolderPage(self.driver, folder_name).wait_for_url()

    @allure.step('Go to the pipeline page: \"{name}\"')
    def go_to_the_pipeline_page(self, name):
        from pages.pipeline_page import PipelinePage
        return self.navigate_to(PipelinePage, self.get_table_item_locator(name), name)
