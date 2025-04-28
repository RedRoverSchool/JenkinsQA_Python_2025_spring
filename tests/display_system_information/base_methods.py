from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common import TimeoutException


class BaseMethods:
    TIMEOUT = 5
    POLL_FREQUENCY = 0.5

    def __init__(self, main_page: WebDriver):
        self.driver = main_page
        self.base_url = main_page.current_url
        self.wait = WebDriverWait(main_page, BaseMethods.TIMEOUT, poll_frequency=BaseMethods.POLL_FREQUENCY)

    def safe_wait(self, condition: callable, timeout: int = None, element_flag: bool = False) -> bool | WebElement | None:
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=BaseMethods.POLL_FREQUENCY)
        try:
            result = wait.until(condition)
            return result if element_flag else True
        except TimeoutException:
            return None if element_flag else False

    def click(self, locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def is_visible(self, locator: tuple[str, str]) -> bool:
        return self.safe_wait(EC.visibility_of_element_located(locator))
