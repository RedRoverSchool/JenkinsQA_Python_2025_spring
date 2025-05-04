from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.freestyle_project_page import FreestyleProjectPage


class FreestyleProjectConfigPage(BasePage):
    class Locator:
        H2 = (By.ID, "general")
        is_enable = (By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')
        is_disable = (By.CLASS_NAME, 'jenkins-toggle-switch__label__unchecked-title')
        is_enable_text = (By.XPATH, '//label[@class="jenkins-toggle-switch__label "]')
        tooltip_enable = (By.XPATH, '//span[@tooltip="Enable or disable the current project"]')
        tooltip_enable_text = (By.XPATH, '//span[@aria-describedby="tippy-15"]')
        SAVE_BUTTON = (By.XPATH, '//button[@name="Submit"]')


    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{project_name}/configure"
        self.name = project_name

    def is_enable(self):
        return self.wait_to_be_visible(self.Locator.is_enable, 5)

    def is_disable(self):
        return self.wait_to_be_visible(self.Locator.is_disable, 5)

    def switch_to_disable(self):
        self.wait_to_be_clickable(self.Locator.is_enable, 5).click()
        return self.is_disable()

    def click_save_button(self):
        from pages.freestyle_project_page import FreestyleProjectPage
        self.wait_to_be_clickable(self.Locator.SAVE_BUTTON).click()
        return FreestyleProjectPage(self.driver, project_name=self.name)

    def is_enable_text(self):
        return self.wait_for_element(self.Locator.tooltip_enable_text).text

    def get_tooltip(self, tooltip_link, tooltip_text):
        actions = ActionChains(self.driver)
        return actions.move_to_element(self.wait_for_element(tooltip_link)).perform()

    def get_tooltip_enable(self):
        return self.get_tooltip(self.Locator.tooltip_enable, self.Locator.tooltip_enable_text)