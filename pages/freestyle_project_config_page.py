from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FreestyleProjectConfigPage(BasePage):
    class Locator:
        H2_LOCATOR = (By.ID, "general")
        ENABLE = (By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')
        DISABLE = (By.CLASS_NAME, 'jenkins-toggle-switch__label__unchecked-title')
        ENABLE_TEXT = (By.XPATH, '//label[@class="jenkins-toggle-switch__label "]')
        TOOLTIP_CONTENT = (By.XPATH, '//div[@class="tippy-content"]')
        DESCRIPTION_FIELD = (By.XPATH, '//textarea[@name="description"]')
        SAVE_BUTTON = (By.XPATH, '//button[@name="Submit"]')
        APPLY_BUTTON = (By.XPATH, '//button[@name="Apply"]')
        PREVIEW = (By.LINK_TEXT, 'Preview')
        HIDE_PREVIEW = (By.LINK_TEXT, 'Hide preview')


    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{project_name}/configure"
        self.name = project_name

    def is_enable(self):
        return self.wait_to_be_visible(self.Locator.ENABLE, 5)

    def is_disable(self):
        return self.wait_to_be_visible(self.Locator.DISABLE, 5)

    def switch_to_disable(self):
        self.wait_to_be_clickable(self.Locator.ENABLE, 5).click()
        return self.is_disable()

    def click_save_button(self):
        from pages.freestyle_project_page import FreestyleProjectPage
        self.wait_to_be_clickable(self.Locator.SAVE_BUTTON).click()
        return FreestyleProjectPage(self.driver, project_name=self.name)

    def click_apply_button(self):
        self.wait_to_be_clickable(self.Locator.APPLY_BUTTON).click()
        return self

    def is_enable_text(self):
        return self.wait_for_element(self.Locator.ENABLE_TEXT).text

    def get_tooltip(self, tooltip_link, tooltip_wait):
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        tooltip = self.find_element(*tooltip_link)
        actions.move_to_element(tooltip).perform()
        self.wait_for_element(tooltip_wait)
        return self.wait_for_element(self.Locator.TOOLTIP_CONTENT).text

    def add_description(self, description_text):
        self.wait_for_element(self.Locator.DESCRIPTION_FIELD).send_keys(description_text)
        return self

    def get_description(self):
        return self.find_element(*self.Locator.DESCRIPTION_FIELD).get_attribute("value")

    def is_preview_visible(self):
        if self.wait_to_be_clickable(self.Locator.PREVIEW):
            return True
        else:
            return False

    def click_preview(self):
        if self.is_preview_visible():
            self.find_element(*self.Locator.PREVIEW).click()
        return self

    def is_hide_preview_visible(self):
        if self.wait_to_be_clickable(self.Locator.HIDE_PREVIEW, 2):
            return True
        else:
            return False
