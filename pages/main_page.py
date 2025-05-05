from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    class Locator:
        NEW_ITEM_BUTTON = (By.LINK_TEXT, "New Item")
        BUILD_HISTORY_BUTTON = (By.LINK_TEXT, "Build History")
        MANAGE_JENKINS_BUTTON = (By.LINK_TEXT, "Manage Jenkins")
        TABLE_ITEM = (By.CSS_SELECTOR, "a.inside")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/"

    def get_item_list(self):
        return [item.text for item in self.find_elements(*self.Locator.TABLE_ITEM)]

    def go_to_new_item_page(self):
        from pages.new_item_page import NewItemPage
        self.wait_to_be_clickable(self.Locator.NEW_ITEM_BUTTON).click()
        return NewItemPage(self.driver).wait_for_url()

    def go_to_build_history_page(self):
        from pages.build_history_page import BuildHistoryPage
        self.wait_to_be_clickable(self.Locator.BUILD_HISTORY_BUTTON).click()
        return BuildHistoryPage(self.driver).wait_for_url()

    def go_to_manage_jenkins_page(self):
        from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage
        self.click_on(self.Locator.MANAGE_JENKINS_BUTTON)
        return ManageJenkinsPage(self.driver).wait_for_url()

