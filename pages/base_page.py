from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from pages.ui_element import UIElementMixin
from pages.components.components import Header


class BasePage(UIElementMixin):
    def __init__(self, driver: WebDriver, timeout = 5):
        super().__init__(driver)
        self.logger.debug(f"{self.__class__.__name__} is being initialized")
        self.base_url = self.config.jenkins.base_url
        self.header = Header(driver)

    def open(self):
        old_url = self.driver.current_url
        self.driver.get(self.url)
        self.logger.debug(f"{self.__class__.__name__} moves to {self.url} from {old_url}")
        return self.wait_for_url()

    def wait_for_url(self):
        try:
            self.wait.until(EC.url_to_be(self.url.replace(" ", "%20")))
        except TimeoutException:
            self.logger.error(f"Timeout when waiting for url {self.url}, current url: {self.driver.current_url}")
        return self

    def get_title(self) -> str:
        return self.driver.title

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_all_windows_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)
        return self.driver
