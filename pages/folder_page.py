from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FolderPage(BasePage):
    class Locators:
        EMPTY_STATE_MESSAGE = (By.XPATH, "//h2")
        CREATE_A_JOB = (By.CSS_SELECTOR, 'a[href="newJob"]')
        TABLE_ITEM = (By.CSS_SELECTOR, "a.inside")

    def __init__(self, driver, *folder_path, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.folder_parts = self.normalize_path_parts(*folder_path)
        self.url = f"{self.base_url}/{self.build_path(*self.folder_parts)}/"

    def get_empty_state_message(self):
        return self.wait_to_be_visible(self.Locators.EMPTY_STATE_MESSAGE).text

    def click_on_create_job_inside_folder(self):
        from pages.new_item_page import NewItemPage
        return self.navigate_to(NewItemPage, self.Locators.CREATE_A_JOB, *self.folder_parts)

    def get_item_list(self):
        return [item.text for item in self.find_elements(*self.Locators.TABLE_ITEM)]
