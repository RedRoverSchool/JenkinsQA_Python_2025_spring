import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FolderPage(BasePage):
    class Locators:
        EMPTY_STATE_MESSAGE = (By.XPATH, "//h2")
        CREATE_A_JOB = (By.CSS_SELECTOR, 'a[href*="newJob"]')
        TABLE_ITEM = (By.CSS_SELECTOR, "a.inside")
        HEADER = (By.CSS_SELECTOR, "h1")


    def __init__(self, driver, folder_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{folder_name}/"

    def wait_for_page(self):
        return self.wait_for_element(self.Locators.CREATE_A_JOB)

    def get_empty_state_message(self):
        return self.wait_to_be_visible(self.Locators.EMPTY_STATE_MESSAGE).text

    @allure.step("Click on \"Create a job\" inside the folder")
    def click_on_create_job_inside_folder(self):
        from pages.new_item_page import NewItemPage
        return self.navigate_to(NewItemPage, self.Locators.CREATE_A_JOB)

    @allure.step("Get list of items from folder")
    def get_item_list(self):
        return [item.text for item in self.find_elements(*self.Locators.TABLE_ITEM)]

    @allure.step("Get header on FolderPage")
    def get_header(self):
        return self.get_header_text(self.Locators.HEADER)
