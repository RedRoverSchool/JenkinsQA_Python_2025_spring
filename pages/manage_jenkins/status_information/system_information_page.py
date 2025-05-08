from selenium.webdriver.common.by import By
from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage
from tests.manage_jenkins.status_information.data import SystemInformationData as SI


class SystemInformationPage(ManageJenkinsPage):
    class Locator:
        TABS_BAR = (By.CSS_SELECTOR, ".tabBar .tab a")
        ACTIVE_TAB = (By.XPATH, "//div[@class='jenkins-tab-pane'][@style='display: block;']/h2")

        @staticmethod
        def tab_table(tab_number: int):
            return By.XPATH, f"//div[@class='jenkins-tab-pane'][{tab_number}]/table/tbody"

        @staticmethod
        def show_all_button(tab_number: int):
            return By.XPATH, f"(//button[contains(normalize-space(text()), 'Show values')])[{tab_number}]"

        @staticmethod
        def hide_all_button(tab_number: int):
            return By.XPATH, f"(//button[contains(normalize-space(text()), 'Hide values')])[{tab_number}]"

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/systemInfo"

    def get_tabs_bar_headers(self) -> list[str]:
        self.wait_to_be_clickable(self.Locator.TABS_BAR)
        return [tab.text.strip() for tab in self.find_elements(*self.Locator.TABS_BAR)]

    def get_active_tab_number(self) -> int:
        tab = self.find_element(*self.Locator.ACTIVE_TAB)
        tab_name = tab.get_attribute("textContent")
        return SI.TABS_BAR_HEADERS.index(tab_name) + 1

    def get_table_content(self) -> list[list[str]]:
        tab_number = self.get_active_tab_number()
        table = self.find_element(*self.Locator.tab_table(tab_number))
        raw_rows = table.find_elements(By.TAG_NAME, "tr")
        processed_rows = []
        for row in raw_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_text = [cell.text for cell in cells]
            processed_rows.append(row_text)
        return processed_rows

    def click_show_all_values_button(self):
        tab_number = self.get_active_tab_number()
        self.click_on(self.Locator.show_all_button(tab_number))

    def click_hide_all_values_button(self):
        tab_number = self.get_active_tab_number()
        self.click_on(self.Locator.hide_all_button(tab_number))
