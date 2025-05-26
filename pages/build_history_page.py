import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BuildHistoryPage(BasePage):
    class Locators:
        TABLE_ITEM = (By.CSS_SELECTOR, "#projectStatus>tbody>tr")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/view/all/builds"

    @allure.step("Get existing builds list.")
    def get_builds_list(self):
        self.wait_to_be_visible_all(self.Locators.TABLE_ITEM, 10)
        item_list = [item.text for item in self.find_elements(*self.Locators.TABLE_ITEM)]
        return item_list
