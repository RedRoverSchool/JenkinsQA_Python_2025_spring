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
        BUILD_NOW_BUTTON = (By.LINK_TEXT, "Build Now")
        BUILDS_NEXT_PAGE_BUTTON = (By.ID, "down")
        BUILDS_PREV_PAGE_BUTTON = (By.ID, "up")
        BUILDS_LINKS = (By.CSS_SELECTOR, "#jenkins-build-history .app-builds-container__item__inner a[href*='job/']")
        BUILDS_LINKS_INNER = (By.CSS_SELECTOR, ".app-builds-container__item__inner__link")

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

    def click_build_now_button(self):
        self.wait_to_be_clickable(self.Locators.BUILD_NOW_BUTTON).click()
        return self

    def get_builds_inner_links(self):
        return self.wait_to_be_visible_all(self.Locators.BUILDS_LINKS_INNER)

    def get_builds_list(self, count):
        self.wait_to_be_visible((By.CSS_SELECTOR, f"#jenkins-builds .app-builds-container__item__inner a[href*='/{count}/']"), 25)
        return self.wait_to_be_visible_all(self.Locators.BUILDS_LINKS, 10)

    # def get_next_page_button(self, count):
    #     self.wait_to_be_visible((By.CSS_SELECTOR, f"#jenkins-builds .app-builds-container__item__inner a[href*='/{count}/']"))
    #
    #     return self.Locators.BUILDS_NEXT_PAGE_BUTTON


    # def click_builds_next_page_button(self):
    #     import time
    #     time.sleep(5)
    #     self.click_on(self.Locators.BUILDS_NEXT_PAGE_BUTTON)
    #     return self

    # def click_builds_prev_page_button(self):
    #     self.scroll_into_view(self.Locators.BUILDS_PREV_PAGE_BUTTON)
    #     self.wait_to_be_clickable(self.Locators.BUILDS_PREV_PAGE_BUTTON, 10).click()
    #     return self
