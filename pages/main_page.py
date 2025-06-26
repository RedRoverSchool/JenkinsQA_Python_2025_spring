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
        TABLE_HEADERS = (By.XPATH, "//table[@id='projectstatus']//thead//th")
        CELLS_IN_JOB_ROW = (By.XPATH, "//td[../td//a[contains(@href, 'job')]]")
        PROJECT_BUTTON = (By.XPATH, "//table[@id='projectstatus']//tbody//td[3]/a")
        TABLE_SVG = (By.CSS_SELECTOR, "td svg")

        @staticmethod
        def table_item_link(name: str):
            return By.LINK_TEXT, quote(name)

        @staticmethod
        def cells_in_job_row(name: str):
            return By.XPATH, f"//tr[@id='job_{name}']/td"

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/"

    @allure.step("Get list of items from \"Dashboard\"")
    def get_item_list(self):
        return [item.text for item in self.find_elements(*self.Locators.TABLE_ITEM)]

    @allure.step("Get actual headers from \"Dashboard\"")
    def get_table_headers_list(self):
        elements = self.find_elements(*self.Locators.TABLE_HEADERS)
        return [el.text.replace("↑", "").replace("↓", "").replace("\n", "").strip()
                for el in elements]

    @allure.step("Get status table data for item '{name}' from Dashboard")
    def get_project_row_data(self, name):
        cells = self.find_elements(*self.Locators.cells_in_job_row(name))
        data = [
            cells[0].find_element(*self.Locators.TABLE_SVG).get_attribute("title"),
            cells[1].find_element(*self.Locators.TABLE_SVG).get_attribute("title"),
            cells[2].find_element(*self.Locators.TABLE_ITEM).text.strip(),
            cells[3].text.strip(),
            cells[4].text.strip(),
            cells[5].text.strip(),
            cells[6].text.strip()
        ]
        self.logger.debug(f" Data row for project '{name}': {data}")
        return data

    @allure.step("Click on Project name")
    def click_on_project(self, name):
        from pages.freestyle_project_page import FreestyleProjectPage
        self.find_element(*self.Locators.PROJECT_BUTTON).click()
        return FreestyleProjectPage(self.driver, name).wait_for_url()

    @allure.step("Go to the New Item Page by clicking New Item button.")
    def go_to_new_item_page(self):
        from pages.new_item_page import NewItemPage
        return self.navigate_to(NewItemPage, self.Locators.NEW_ITEM_BUTTON)

    @allure.step("Go to the Build History page by clicking Build History button.")
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
        return self.navigate_to(FolderPage, self.Locators.table_item_link(name), name)

    @allure.step("Go to the Freestyle project page by clicking project link.")
    def go_to_freestyle_project_page(self, name):
        from pages.freestyle_project_page import FreestyleProjectPage
        return self.navigate_to(FreestyleProjectPage, self.Locators.table_item_link(name), name)

    @allure.step("Expand build queue info block if it is collapsed.")
    def show_build_queue_info_block(self):
        if self.wait_to_be_visible(self.Locators.BUILD_QUEUE_BLOCK).get_attribute("class").__contains__("collapsed"):
            self.wait_for_element(self.Locators.BUILD_QUEUE_TOGGLE).click()

    @allure.step("Wait for Jenkins build queue to start, finish, and clear.")
    def wait_for_build_queue_executed(self):
        self.show_build_queue_info_block()
        with allure.step("Wait for the build to start and the 'Build Queue (1)' header to appear."):
            logger.info("Getting message 'Build Queue (1)'")
            self.wait_text_to_be_present(self.Locators.BUILD_QUEUE_HEADER, "Build Queue (1)", 10)
        with allure.step("Wait for the build finished and the \"Build Queue\" header to appear."):
            logger.info("Getting message 'Build Queue'")
            self.wait_text_to_be_present(self.Locators.BUILD_QUEUE_HEADER, "Build Queue", 10)
        with allure.step("Wait for the message \"No builds in the queue.\" to appear."):
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
        return self.navigate_to(PipelinePage, self.Locators.table_item_link(name), name)

    @allure.step("Go to the Pipeline page by clicking the pipeline \"{name}\" link.")
    def go_to_pipeline_page(self, name):
        from pages.pipeline_page import PipelinePage
        self.wait_to_be_clickable(self.Locators.TABLE_ITEM).click()
        return PipelinePage(self.driver, name).wait_for_url()

    @allure.step('Go to the organization folder page: \"{project_name}\"')
    def go_to_the_organization_folder_page(self, project_name):
        from pages.organization_folder_page import OrganizationFolderPage
        self.wait_to_be_clickable(self.Locators.PROJECT_BUTTON).click()
        return OrganizationFolderPage(self.driver, project_name).wait_for_url()
