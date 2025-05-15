from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FreestyleProjectPage(BasePage):
    class Locators:
        H1 = (By.CSS_SELECTOR, '.job-index-headline.page-headline')
        WARNING_MESSAGE = (By.XPATH, '//form[@action="enable"]')
        FORM = (By.XPATH, '//form[@action="enable"]')
        BUILD_NOW = (By.LINK_TEXT, 'Build Now')
        ENABLE_BUTTON = (By.XPATH, '//button[@name="Submit"]')
        CONFIGURE_MENU_ITEM = (By.LINK_TEXT, 'Configure')
        DESCRIPTION = (By.ID, 'description')
        MENU_ITEMS = (By.XPATH, '//div[@class="task "]')
        BUILDS_LINK = (By.CSS_SELECTOR, "#jenkins-build-history>div>span~div a")

    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + self.get_part_url(project_name)
        self.name = project_name

    def click_enable_button(self):
        self.wait_for_element(self.Locators.ENABLE_BUTTON).click()
        self.wait_for_element(self.Locators.BUILD_NOW)
        return self

    def get_part_url(self, name: str):
        if len(name.split(' ')) > 1:
            new_name = name.replace(" ", "%20")
        else:
            new_name = name
        return f"/job/{new_name}/"

    def get_warning_message(self):
        self.wait_text_to_be_present(self.Locators.H1, self.name)
        if len(self.find_elements(*self.Locators.FORM)) > 0:
            return self.wait_to_be_visible(self.Locators.WARNING_MESSAGE).text
        else:
            return ''

    def get_h1_value(self):
        self.wait_to_be_clickable(self.Locators.BUILD_NOW)
        return self.wait_for_element(self.Locators.H1).text

    def get_description(self):
        return self.wait_for_element(self.Locators.DESCRIPTION).text

    def get_title(self):
        self.wait_for_element(self.Locators.BUILD_NOW)
        return self.driver.title

    def go_to_configure(self):
        from pages.freestyle_project_config_page import FreestyleProjectConfigPage
        self.wait_for_element(self.Locators.BUILD_NOW)
        self.wait_to_be_clickable(self.Locators.CONFIGURE_MENU_ITEM).click()
        return FreestyleProjectConfigPage(self.driver, self.name)

    def get_menu_items_texts(self):
        return [item.text for item in self.wait_to_be_visible_all(self.Locators.MENU_ITEMS)]

    def wait_for_build_executed(self, timeout):
        self.wait_for_element(self.Locators.BUILDS_LINK, timeout)
        return self
