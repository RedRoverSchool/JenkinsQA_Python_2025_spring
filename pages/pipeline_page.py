import allure
import logging
from urllib.parse import quote

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.main_page import MainPage
from tests.new_item.data import new_folder_name

logger = logging.getLogger(__name__)


class PipelinePage(BasePage):
    class Locators:
        DESCRIPTION_ELEMENT = (By.ID, "description")
        MOVE_LINK = (By.XPATH, '//a[contains(@href, "/move")]')
        MOVE_BTN = (By.XPATH, "//button[@name='Submit']")
        SETTING_INPUT = (By.XPATH, "//select[@name='destination']")
        HEADER = (By.TAG_NAME, "h1")
        BUILDS_LINKS = (By.CSS_SELECTOR, "#jenkins-build-history a.app-builds-container__item__inner__link")
        BUILDS_NEXT_PAGE_BUTTON = (By.ID, "down")
        BUILDS_PREV_PAGE_BUTTON = (By.ID, "up")
        SINGLE_BUILD_NUMBER = (By.CLASS_NAME, "app-builds-container__item__inner__link")

    def __init__(self, driver, pipeline_project_name, timeout=10):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{quote(pipeline_project_name)}/"

    def get_value_name(self, name: str) -> tuple[str, str]:
        return (By.CSS_SELECTOR, f'[value="/{name}"]')

    def is_description_element_displayed(self):
        return self.wait_for_element(self.Locators.DESCRIPTION_ELEMENT).is_displayed()

    def get_description_text(self):
        return self.wait_for_element(self.Locators.DESCRIPTION_ELEMENT).text

    def click_move_link(self):
        self.wait_to_be_clickable(self.Locators.MOVE_LINK).click()
        return self

    def open_move_destination_list(self):
        self.wait_to_be_visible(self.Locators.SETTING_INPUT, timeout=10).click()
        return self

    def choose_move_location(self):
        self.wait_to_be_visible(self.get_value_name(new_folder_name)).click()
        return self

    def click_submit_btn(self):
        self.wait_to_be_clickable(self.Locators.MOVE_BTN).click()
        return self

    def move_item_to_folder(self):
        self.click_move_link()
        self.open_move_destination_list()
        self.choose_move_location()
        self.click_submit_btn()
        return MainPage(self.driver)

    @allure.step("Get the page header text")
    def get_header_pipeline_page(self) -> str:
        return self.get_visible_text(self.Locators.HEADER)

    @allure.step("Get builds list in Builds History section.")
    def get_builds_list(self):
        return self.wait_to_be_visible_all(self.Locators.BUILDS_LINKS, 10)

    @allure.step("Get \"Next page\" button")
    def get_next_page_button(self):
        self.scroll_to_the_end_of_builds_list()
        return self.wait_to_be_visible(self.Locators.BUILDS_NEXT_PAGE_BUTTON, 10)

    @allure.step("Get \"Previous page\" button")
    def get_previous_page_button(self):
        self.scroll_to_the_end_of_builds_list()
        return self.wait_to_be_visible(self.Locators.BUILDS_PREV_PAGE_BUTTON, 10)

    @allure.step("Scroll to the end of builds list")
    def scroll_to_the_end_of_builds_list(self):
        builds = self.get_builds_list()
        last_build_link = builds[-1]
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", last_build_link)
        return self

    @allure.step("Scroll to the top of builds list")
    def scroll_to_the_top_of_builds_list(self):
        builds = self.get_builds_list()
        first_build_link = builds[0]
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", first_build_link)
        return self

    @allure.step("Click \"Next page\" button")
    def click_next_page_button(self):
        logger.info("Scroll to the ends")
        self.scroll_to_the_end_of_builds_list()
        logger.info("Click next")
        self.click_on(self.Locators.BUILDS_NEXT_PAGE_BUTTON, 10)
        logger.info("Scroll to the top")
        self.scroll_to_the_top_of_builds_list()
        return self

    @allure.step("Click \"Previous page\" button")
    def click_previous_page_button(self):
        self.scroll_to_the_end_of_builds_list()
        self.click_on(self.Locators.BUILDS_PREV_PAGE_BUTTON, 10)
        self.scroll_to_the_top_of_builds_list()
        return self

    @allure.step("Get single build number")
    def get_single_build_number(self):
        return self.get_visible_text(self.Locators.SINGLE_BUILD_NUMBER).splitlines()[0]
