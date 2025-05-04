from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FreestyleProjectPage(BasePage):
    class Locator:
        warning_message = (By.XPATH, '//form[@action="enable"]')
        build_now = (By.LINK_TEXT, 'Build Now')
        enable_button = (By.XPATH, '//button[@name="Submit"]')
        configure_menu = (By.LINK_TEXT, 'Configure')

    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{project_name}"
        self.name = project_name

    def get_warning_message(self):
        try:
            return self.wait_to_be_visible(self.Locator.warning_message, 1).text
        except Exception:
            pass
            return ''

    def click_enable_button(self):
        self.wait_to_be_clickable(self.Locator.enable_button).click()
        self.wait_for_element(self.Locator.build_now)
        return self

    def go_to_configure(self):
        from pages.freestyle_project_config_page import FreestyleProjectConfigPage
        self.wait_to_be_clickable(self.Locator.configure_menu).click()
        return FreestyleProjectConfigPage(self.driver, self.name)