import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from tests.manage_jenkins.data import ManageJenkinsData as MJ


class ManageJenkinsPage(BasePage):
    class Locator:
        PLUGINS = (By.XPATH, "//a[@href='pluginManager']/..")
        class StatusInformation:
            SYSTEM_INFORMATION = (By.XPATH, "//a[@href='systemInfo']/..")
            LOAD_STATISTICS = (By.XPATH, "//a[@href='load-statistics']/..")

        @staticmethod
        def get_timespan_graph(flag_value: str) -> tuple[str, str]:
            return By.XPATH, f"//img[contains(@src, '{flag_value}')]"

        TIMESPAN_DROPDOWN = (By.ID, "timespan-select")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/"

    @allure.step("Go to System Information page")
    def go_to_system_information_page(self):
        from pages.manage_jenkins.status_information.system_information_page import SystemInformationPage
        self.click_on(self.Locator.StatusInformation.SYSTEM_INFORMATION)
        return SystemInformationPage(self.driver).wait_for_url()

    @allure.step("Go to Load Statistics page")
    def go_to_load_statistics_page(self):
        from pages.manage_jenkins.status_information.load_statistics_page import LoadStatisticsPage
        self.click_on(self.Locator.StatusInformation.LOAD_STATISTICS)
        return LoadStatisticsPage(self.driver).wait_for_url()

    @allure.step("Go to Plugins Page")
    def go_to_plugins_page(self):
        from pages.manage_jenkins.plugins.plugins_page import PluginsPage
        self.click_on(self.Locator.PLUGINS)
        return PluginsPage(self.driver).wait_for_url()

    @allure.step("Select timespan option")
    def select_timespan(self, option: str) -> None:
        element = self.wait_to_be_visible(self.Locator.TIMESPAN_DROPDOWN, timeout=5)
        Select(element).select_by_visible_text(option)

    @allure.step("Get graph for selected timespan option")
    def get_graph_for_selected_timespan_option(self, option: str) -> WebElement | bool:
        self.select_timespan(option)
        graph_locator = self.Locator.get_timespan_graph(MJ.TIMESPAN_OPTIONS.get(option))
        try:
            return self.wait_to_be_visible(graph_locator, timeout=5)
        except TimeoutException:
            return False
