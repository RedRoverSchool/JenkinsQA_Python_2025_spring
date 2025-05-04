from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.settings import Config


class BasePage:
    class Locators:
        HEADER_LOGO = (By.ID, "jenkins-home-link")


    def __init__(self, driver: WebDriver, timeout = 5):
        self.config = Config.load()
        self.base_url = self.config.jenkins.base_url
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def open(self):
        self.driver.get(self.url)
        return self.wait_for_url()

    def wait_for_url(self):
        self.wait.until(EC.url_to_be(self.url))
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

    def go_to_the_main_page(self):
        from pages.main_page import MainPage
        self.wait_to_be_clickable(self.Locators.HEADER_LOGO).click()
        return MainPage(self.driver)