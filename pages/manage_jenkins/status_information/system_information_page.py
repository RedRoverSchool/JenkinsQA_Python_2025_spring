from selenium.webdriver.common.by import By
from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage


class SystemInformationPage(ManageJenkinsPage):
    class Locator:
        TABS_BAR = (By.CSS_SELECTOR, ".tabBar .tab a")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/systemInfo"

    def get_tabs_bar_headers(self) -> list[str]:
        self.wait_to_be_clickable(self.Locator.TABS_BAR)
        return [tab.text.strip() for tab in self.find_elements(*self.Locator.TABS_BAR)]
