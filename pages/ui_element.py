import logging

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from core.settings import Config


class UIElementMixin:
    def __init__(self, driver: WebDriver, timeout=5):
        self.driver = driver
        self.config = Config.load()
        self.wait = WebDriverWait(driver, timeout=timeout)
        self.logger = logging.getLogger(self.__class__.__name__)

    def find_element(self, by, selector):
        return self.driver.find_element(by, selector)

    def find_elements(self, by, selector):
        return self.driver.find_elements(by, selector)

    def _wait_for(self, timeout, condition, *args):
        try:
            self.logger.debug(f"waiting for {condition.__name__}{args}")
            return WebDriverWait(self.driver, timeout).until(condition(*args))
        except TimeoutException:
            self.logger.error(f"Timeout when waiting for {condition.__name__}{args}")
            raise

    def wait_for_element(self, locator, timeout=5) -> WebElement:
        return self._wait_for(timeout, EC.presence_of_element_located, locator)

    def wait_to_be_clickable(self, locator, timeout=5) -> WebElement:
        return self._wait_for(timeout, EC.element_to_be_clickable, locator)

    def wait_to_be_visible(self, locator, timeout=5) -> WebElement:
        return self._wait_for(timeout, EC.visibility_of_element_located, locator)

    def wait_to_be_visible_all(self, locator, timeout=5) -> list[WebElement]:
        return self._wait_for(timeout, EC.visibility_of_all_elements_located, locator)

    def wait_text_to_be_present(self, locator, text, timeout=5) -> bool:
        return self._wait_for(timeout, EC.text_to_be_present_in_element, locator, text)

    def wait_for_new_window(self, num_windows = 2):
        return self.wait.until(EC.number_of_windows_to_be(num_windows))

    def wait_element_to_disappear(self, locator, timeout=5) -> bool:
        return self._wait_for(timeout, EC.invisibility_of_element_located, locator)

    def click_on(self, locator, timeout=5) -> None:
        self.logger.debug(f"Click on locator {locator}")
        self._wait_for(timeout, EC.element_to_be_clickable, locator).click()

    def enter_text(self, locator, text):
        return self.wait_for_element(locator).send_keys(text)

    def get_value(self, locator) -> str | None:
        return self.wait_to_be_visible(locator).get_attribute("value")

    def wait_and_get_attribute(self, locator, attribute_name) -> str:
        return self.wait_for_element(locator).get_attribute(attribute_name)

    def scroll_into_view(self, element):
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center", inline: "center"})',
            element)
        return self

    def scroll_to_element(self, By, Selector):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(By, Selector)).perform()
        return self

    def navigate_to(self, page_class, *args):
        with allure.step(f"Navigate to \"{page_class.__name__}\""):
            self.logger.debug(f"Navigating to {page_class.__name__} with click on {args}")
            if len(args) == 1:
                locator = args[0]
            elif len(args) > 1:
                locator, args = args
            else:
                raise ValueError("Not enough arguments")
            self.wait_to_be_clickable(locator).click()
            if not isinstance(args, str):
                return page_class(self.driver, *args).wait_for_url()
            else:
                return page_class(self.driver, args).wait_for_url()

    def get_header_text(self, locator):
        header = self.wait_to_be_visible(locator)
        return header.text

    def get_text(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    def check_checkbox(self, checkbox):
        self.scroll_into_view(checkbox)
        self.wait_to_be_clickable(checkbox).click()
        return self

    def get_visible_text(self, locator) -> str:
        return self.wait_to_be_visible(locator).text.strip()

    def get_visible_text_lines(self, locator) -> list[str]:
        return self.get_visible_text(locator).splitlines()

    def is_element_selected(self, locator) -> bool:
        return self.wait_for_element(locator).is_selected()

    def hover_over_element(self, locator):
        element = self.wait_to_be_visible(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        return element
