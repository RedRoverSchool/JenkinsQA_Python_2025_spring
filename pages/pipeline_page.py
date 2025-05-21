import logging
from urllib.parse import quote

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.main_page import MainPage
from tests.new_item.data import new_folder_name

logger = logging.getLogger(__name__)


class PipelinePage(BasePage):
    class Locator:
        DESCRIPTION_ELEMENT = (By.ID, "description")
        MOVE_LINK = (By.XPATH, '//a[contains(@href, "/move")]')
        MOVE_BTN = (By.XPATH, "//button[@name='Submit']")
        SETTING_INPUT = (By.XPATH, "//select[@name='destination']")

    def __init__(self, driver, pipeline_project_name, timeout=10):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{quote(pipeline_project_name)}/"

    def get_value_name(self, name: str) -> tuple[str, str]:
        return (By.CSS_SELECTOR, f'[value="/{name}"]')

    def is_description_element_displayed(self):
        return self.wait_for_element(self.Locator.DESCRIPTION_ELEMENT).is_displayed()

    def get_description_text(self):
        return self.wait_for_element(self.Locator.DESCRIPTION_ELEMENT).text

    def click_move_link(self):
        self.wait_to_be_clickable(self.Locator.MOVE_LINK).click()
        return self

    def open_move_destination_list(self):
        self.wait_to_be_clickable(self.Locator.SETTING_INPUT, timeout=5).click()
        return self

    def choose_move_location(self):
        self.wait_to_be_visible(self.get_value_name(new_folder_name)).click()
        return self

    def click_submit_btn(self):
        self.wait_to_be_clickable(self.Locator.MOVE_BTN).click()
        return self

    def move_item_to_folder(self):
        self.click_move_link()
        self.open_move_destination_list()
        self.choose_move_location()
        self.click_submit_btn()
        self.header.go_to_the_main_page()
        return MainPage(self.driver)
