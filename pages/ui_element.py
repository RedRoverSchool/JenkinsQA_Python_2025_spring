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

    def wait_for_elements(self, locator, timeout=5) -> list[WebElement]:
        return self._wait_for(timeout, EC.presence_of_all_elements_located, locator)

    def wait_to_be_clickable(self, locator, timeout=5) -> WebElement:
        return self._wait_for(timeout, EC.element_to_be_clickable, locator)

    def wait_element_to_be_clickable(self, element: WebElement, timeout=5) -> WebElement:
        return self._wait_for(timeout, EC.element_to_be_clickable, element)

    def wait_to_be_visible(self, locator, timeout=5) -> WebElement:
        return self._wait_for(timeout, EC.visibility_of_element_located, locator)

    def wait_to_be_visible_all(self, locator, timeout=5) -> list[WebElement]:
        return self._wait_for(timeout, EC.visibility_of_all_elements_located, locator)

    def wait_to_be_visible_element(self, element: WebElement, timeout=5) -> WebElement:
        return self._wait_for(timeout, EC.visibility_of, element)

    def wait_text_to_be_present(self, locator, text, timeout=5) -> bool:
        return self._wait_for(timeout, EC.text_to_be_present_in_element, locator, text)

    def wait_for_new_window(self, num_windows = 2):
        return self.wait.until(EC.number_of_windows_to_be(num_windows))

    def wait_element_to_disappear(self, locator, timeout=10) -> bool:
        return self._wait_for(timeout, EC.invisibility_of_element_located, locator)

    def _scroll_wait(self, element: WebElement) -> WebElement:
        self.scroll_into_view(element)
        return self.wait_to_be_visible_element(element)

    def click_on(self, locator, timeout=5) -> None:
        self.logger.debug(f"Click on locator {locator}")
        self._wait_for(timeout, EC.element_to_be_clickable, locator).click()

    def scroll_and_click(self, locator) -> None:
        element = self.wait_for_element(locator)
        self.scroll_wait_click(element)

    def click_elements(self, locator: tuple) -> "UIElementMixin":
        clickable_elements = self.wait_for_elements(locator)
        [self.scroll_into_view(el).wait_to_be_clickable(el).click() for el in clickable_elements]
        return self

    def enter_text(self, locator, text) -> None:
        return self.wait_for_element(locator).send_keys(text)

    def get_value(self, locator) -> str | None:
        return self.wait_to_be_visible(locator).get_attribute("value")

    def wait_and_get_attribute(self, locator, attribute_name) -> str:
        return self.wait_to_be_visible(locator).get_attribute(attribute_name)

    def wait_and_get_attribute_with_scroll(self, locator: tuple, attribute_name: str) -> str:
        element = self.wait_for_element(locator)
        return self.scroll_wait_get_attribute(element, attribute_name)

    def get_attributes_with_scroll(self, locator: tuple, attribute_name: str) -> list[str]:
        elements = self.wait_for_elements(locator)
        return [self.scroll_and_get_attribute(el, attribute_name) for el in elements]

    def scroll_into_view(self, element):
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center", inline: "center"})',
            element)
        return self

    def scroll_and_get_element(self, element: WebElement) -> WebElement:
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center", inline: "center"})',
            element
        )
        return element

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

    def get_visible_text_with_scroll(self, locator) -> str:
        element = self.wait_for_element(locator)
        return self.get_clean_text_from_element_with_scroll(element)

    def get_clean_texts_from_elements(self, locator) -> list[str]:
        elements = self.wait_for_elements(locator)
        return [self.get_clean_text_from_element_with_scroll(el) for el in elements]

    def get_visible_text_lines(self, locator) -> list[str]:
        return self.get_visible_text(locator).splitlines()

    def is_element_selected(self, locator) -> bool:
        return self.wait_for_element(locator).is_selected()

    def is_elements_selected(self, locator) -> list[bool]:
        elements = self.wait_for_elements(locator)
        return [el.is_selected() for el in elements]

    def is_elements_unselected(self, locator) -> list[bool]:
        return [not state for state in self.is_elements_selected(locator)]

    def hover_over_element(self, target) -> WebElement:
        element = self.wait_to_be_visible(target) if isinstance(target, tuple) else target
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def is_element_displayed(self, locator) -> bool:
        return self.wait_to_be_visible(locator).is_displayed()

    def is_elements_displayed(self, locator) -> list[bool]:
        elements = self.wait_for_elements(locator)
        return [self.scroll_and_get_element(el).is_displayed() for el in elements]

    def is_displayed_with_scroll(self, locator) -> bool:
        element = self.wait_for_element(locator)
        return self.scroll_wait_displayed(element)

    def scroll_wait_click(self, element: WebElement) -> None:
        self.scroll_into_view(element).wait_element_to_be_clickable(element)
        element.click()

    def get_tooltip_text(self, icon_element: WebElement, tooltip_locator) -> str:
        try:
            self.scroll_into_view(icon_element)
            self.hover_over_element(icon_element)
            return self.wait_to_be_visible(tooltip_locator).text.strip()
        except TimeoutException:
            self.logger.error("Tooltip did not appear for locator: %s", tooltip_locator)
            return ""

    def wait_until_tooltip_disappears(self, icon_element: WebElement, tooltip_locator, hover_out_locator) -> bool:
        try:
            self.scroll_into_view(icon_element)
            self.hover_over_element(icon_element)
            self.wait_to_be_visible(tooltip_locator)
            self.hover_over_element(hover_out_locator)
            return self.wait_element_to_disappear(tooltip_locator)
        except TimeoutException:
            self.logger.error("Tooltip did not disappear for locator: %s", tooltip_locator)
            return False

    def get_clean_text_from_element_with_scroll(self, element: WebElement) -> str:
        try:
            return self._scroll_wait(element).text.strip()
        except TimeoutException:
            self.logger.error("Timeout: WebElement not visible to get text")
            return ""

    def scroll_wait_displayed(self, element: WebElement) -> bool:
        try:
            self.scroll_into_view(element)
            return self.wait_to_be_visible_element(element).is_displayed()
        except TimeoutException:
            self.logger.error("Timeout: WebElement not visible")
            return False

    def scroll_wait_get_attribute(self, element: WebElement, attribute_name: str) -> str:
        try:
            return self._scroll_wait(element).get_attribute(attribute_name)
        except TimeoutException:
            self.logger.error("Element not visible for reading attribute '%s'", attribute_name)
            return ""

    def scroll_and_get_attribute(self, element: WebElement, attribute_name: str) -> str:
        try:
            self.scroll_into_view(element)
            return element.get_attribute(attribute_name)
        except TimeoutException:
            self.logger.error("Element not visible for reading attribute '%s'", attribute_name)
            return ""

    def get_tooltip_texts(self, el_locator, tooltip_locator) -> list[str]:
        elements = self.wait_for_elements(el_locator)
        return [self.get_tooltip_text(el, tooltip_locator) for el in elements]

    def wait_all_tooltips_to_disappear(self, icon_locator, tooltip_locator, hover_out_locator) -> list[bool]:
        elements = self.wait_for_elements(icon_locator)
        return [self.wait_until_tooltip_disappears(el, tooltip_locator, hover_out_locator) for el in elements]
