from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FreestyleProjectPage(BasePage):
    class Locator:
        PAGE_HEADER = (By.CSS_SELECTOR, ".page-headline")


    def __init__(self, driver, name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{name}/"
