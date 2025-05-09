from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ManageJenkinsPage(BasePage):
    class Locator:
        class StatusInformation:
            SYSTEM_INFORMATION = (By.XPATH, "//a[@href='systemInfo']/..")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/"

    def go_to_system_information_page(self):
        from pages.manage_jenkins.status_information.system_information_page import SystemInformationPage
        self.click_on(self.Locator.StatusInformation.SYSTEM_INFORMATION)
        return SystemInformationPage(self.driver).wait_for_url()
