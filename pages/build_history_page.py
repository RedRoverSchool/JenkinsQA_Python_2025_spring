from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BuildHistoryPage(BasePage):
    class Locators:
        TABLE_ITEM = (By.CSS_SELECTOR, "#projectStatus>tbody>tr")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/view/all/builds"

    def get_build_list(self):
        self.wait_to_be_visible_all(self.Locators.TABLE_ITEM, 10)
        item_list = [item.text for item in self.find_elements(*self.Locators.TABLE_ITEM)]
        from core.jenkins_utils import get_build_info, get_job_info
        for name in item_list:
            name = name.split()[0]
            get_job_info(self.driver, name, self.config)
            get_build_info(self.driver, name, self.config)
        return item_list
