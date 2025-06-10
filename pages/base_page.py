import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.ui_element import UIElementMixin
from pages.components.components import Header


class BasePage(UIElementMixin):
    def __init__(self, driver: WebDriver, timeout=5):
        super().__init__(driver)
        self.timeout = timeout
        self.base_url = self.config.jenkins.base_url
        self.header = Header(driver)

    def open(self):
        self.driver.get(self.url)
        return self.wait_for_url()

    def wait_for_url(self):
        if hasattr(self, "wait_for_page") and callable(self.wait_for_page):
            self.logger.debug(f"Waiting for page content to load: {self.url}")
            try:
                self.wait_for_page()
                self.logger.debug(f"Page content loaded: {self.url}")
                return self
            except TimeoutException:
                self.logger.error(f"Timeout while waiting for page content: {self.url}")
        try:
            self.wait.until(EC.url_to_be(self.url.replace(" ", "%20")))
        except TimeoutException:
            self.logger.error(f"Timeout when waiting for url {self.url}, current url: {self.driver.current_url}")
        return self

    @allure.step("Get the current page title")
    def get_title(self) -> str:
        return self.driver.title

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_all_windows_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)
        return self.driver
