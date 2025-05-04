import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from core.settings import Config

class BasePage:
    class Locators:
        HEADER_LOGO = (By.ID, "jenkins-home-link")
        USER_PAGE_LINK = (By.CSS_SELECTOR, "a[href*='/user/']")


    def __init__(self, driver: WebDriver, timeout = 5):
        self.config = Config.load()
        self.base_url = self.config.jenkins.base_url
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)
        self.logger = logging.getLogger(self.__class__.__name__)

    def open(self):
        self.driver.get(self.url)
        return self.wait_for_url()

    def wait_for_url(self):
        try:
            self.wait.until(EC.url_to_be(self.url))
        except TimeoutException:
            self.logger.error(f"Timeout when waiting for url {self.url}, current url: {self.driver.current_url}")
        return self

    def find_element(self, by, selector):
        return self.driver.find_element(by, selector)

    def find_elements(self, by, selector):
        return self.driver.find_elements(by, selector)

    def _wait_for(self, locator, condition, timeout):
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def wait_for_element(self, locator, timeout = 5) -> WebElement:
        return self._wait_for(locator, EC.presence_of_element_located, timeout)

    def wait_to_be_clickable(self, locator, timeout = 5) -> WebElement:
        return self._wait_for(locator, EC.element_to_be_clickable, timeout)

    def wait_to_be_visible(self, locator, timeout = 5) -> WebElement:
        return self._wait_for(locator, EC.visibility_of_element_located, timeout)

    def wait_to_be_visible_all(self, locator, timeout = 5) -> [WebElement]:
        return self._wait_for(locator, EC.visibility_of_all_elements_located, timeout)

    def go_to_the_main_page(self):
        from pages.main_page import MainPage
        self.wait_to_be_clickable(self.Locators.HEADER_LOGO).click()
        return MainPage(self.driver)

    def go_to_the_user_page(self):
        from pages.user_page import UserPage
        self.wait_to_be_clickable(self.Locators.USER_PAGE_LINK).click()
        return UserPage(self.driver, self.get_username())

    def scroll_into_view(self, element):
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center", inline: "center"})',
            element)

    def get_current_window_handle(self):
        return self.driver.window_handles[0]

    def switch_to_new_window(self):
        self.driver.switch_to.new_window()
        return self.driver

    def switch_to(self, page_window):
        self.driver.switch_to.window(page_window)

    def get_username(self):
        return self.config.jenkins.USERNAME

    def get_password(self):
        return self.config.jenkins.PASSWORD

    def get_server(self):
        return f"{self.config.jenkins.HOST}:{self.config.jenkins.PORT}"
