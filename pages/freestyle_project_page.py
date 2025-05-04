from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FreestyleProjectPage(BasePage):
    class Locator:
        H1 = (By.CSS_SELECTOR, '.job-index-headline.page-headline')
        WARNING_MESSAGE = (By.XPATH, '//form[@action="enable"]')
        FORM = (By.XPATH, '//form[@action="enable"]')
        BUILD_NOW = (By.LINK_TEXT, 'Build Now')
        ENABLE_BUTTON = (By.XPATH, '//button[@name="Submit"]')
        CONFIGURE_MENU_ITEM = (By.LINK_TEXT, 'Configure')


    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{project_name}"
        self.name = project_name

    def get_name(self):
        return self.name

    def get_warning_message(self):
        self.wait_text_to_be_present(self.Locator.H1, f"{self.name}")
        if len(self.find_elements(*self.Locator.FORM)) > 0:
            return self.wait_to_be_visible(self.Locator.WARNING_MESSAGE).text
        else:
            return ''

    def click_enable_button(self):
        self.wait_for_element(self.Locator.ENABLE_BUTTON).click()
        return self

    def go_to_configure(self):
        from pages.freestyle_project_config_page import FreestyleProjectConfigPage
        self.wait_for_element(self.Locator.BUILD_NOW)
        self.wait_to_be_clickable(self.Locator.CONFIGURE_MENU_ITEM).click()
        return FreestyleProjectConfigPage(self.driver, self.name)