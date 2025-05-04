from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class FreestyleProjectConfigPage(BasePage):
    class Locator:
        GENERAL_BUTTON = (By.ID, "general")
        ADD_BUILD_STEP_BUTTON = (
            By.XPATH, "//button[@class='jenkins-button hetero-list-add' and @suffix='builder']"
        )
        BUILD_STEPS_LIST = (By.XPATH, "//button[@class='jenkins-dropdown__item ']")

    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{project_name}/configure"

    def get_add_build_step_button(self):
        button = self.find_element(*self.Locator.ADD_BUILD_STEP_BUTTON)
        return button

    def get_build_steps_list(self):
        button = self.get_add_build_step_button()
        button.send_keys(Keys.END)
        button.click()
        self.wait_to_be_clickable(self.Locator.BUILD_STEPS_LIST)
        return self.find_elements(*self.Locator.BUILD_STEPS_LIST)
