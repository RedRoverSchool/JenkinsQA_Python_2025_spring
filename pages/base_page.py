from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.ui_element import UIElementMixin
from pages.components.components import Header


class BasePage(UIElementMixin):
    def __init__(self, driver: WebDriver, timeout = 5):
        super().__init__(driver)
        self.timeout = timeout
        self.base_url = self.config.jenkins.base_url
        self.header = Header(driver)

    def open(self):
        self.driver.get(self.url)
        return self.wait_for_url()

    def wait_for_url(self):
        try:
            self.wait.until(EC.url_to_be(self.url.replace(" ", "%20")))
        except TimeoutException:
            self.logger.error(f"Timeout when waiting for url {self.url}, current url: {self.driver.current_url}")
        return self


    def get_title(self) -> str:
        return self.driver.title

    def is_element_present(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    def get_header_text(self):
        header = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        return header.text

    def is_header_contains(self, text):
        return text in self.get_header_text()

    def get_text(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text