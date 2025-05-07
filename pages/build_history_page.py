from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BuildHistoryPage(BasePage):
    class Locator:
        TABLE_ITEM = (By.CSS_SELECTOR, "#projectStatus>tbody>tr")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/view/all/builds"

    def get_build_list(self):
        self.wait_to_be_visible_all(self.Locator.TABLE_ITEM, 10)
        return [item.text for item in self.find_elements(*self.Locator.TABLE_ITEM)]
