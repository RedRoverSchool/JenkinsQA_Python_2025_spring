from tests.display_system_information.base_methods import BaseMethods
from tests.display_system_information.system_information_page import SystemInformationPage as SIP
from tests.display_system_information.locators import (
    JenkinsSidePanel as SP,
    ManageJenkinsTask as MJ,
    SystemInformationPage as SI)


class TestSystemInformationSection:
    def test_open_system_information_page(self, main_page):
        page = BaseMethods(main_page)
        page.click(SP.MANAGE_JENKINS)
        page.click(MJ.SYSTEM_INFORMATION)
        assert page.is_visible(SI.TABS_BAR)

    def test_system_properties_tab_show_hide_all_values(self, sys_info_page):
        page = SIP(sys_info_page)
        element_names = page.get_all_element_names(SI.SHOW_SYS_VALUES_BUTTON)
        assert len(element_names) > 0

        page.click(SI.SHOW_SYS_VALUES_BUTTON)
        for element_name in element_names:
            assert page.is_value_displayed(element_name), f'Value for {element_name} is still hidden'

        page.click(SI.HIDE_SYS_VALUES_BUTTON)
        for element_name in element_names:
            button_locator = page.define_show_single_value_button_locator(element_name)
            assert page.is_clickable(button_locator), f'Button for {element_name} is not clickable'

    def test_system_properties_tab_show_hide_each_single_value(self, sys_info_page):
        page = SIP(sys_info_page)
        element_names = page.get_all_element_names(SI.SHOW_SYS_VALUES_BUTTON)
        assert len(element_names) > 0, 'List of system properties is empty'

        for element_name in element_names:
            show_button = page.define_show_single_value_button_locator(element_name)
            page.click(show_button)
            assert page.is_value_displayed(element_name), f'Value for {element_name} is still hidden'

            hide_button = page.define_hide_single_value_button_locator(element_name)
            page.click(hide_button)
            assert page.is_clickable(show_button), f'Button for {element_name} is not clickable'

    def test_environment_variables_tab_show_hide_all_values(self, sys_info_page):
        page = SIP(sys_info_page)
        page.click(SI.ENVIRONMENT_VARIABLES_TAB)
        element_names = page.get_all_element_names(SI.SHOW_ENV_VALUES_BUTTON)
        assert len(element_names) > 0

        page.click(SI.SHOW_ENV_VALUES_BUTTON)
        for element_name in element_names:
            assert page.is_value_displayed(element_name), f'Value for {element_name} is still hidden'

        page.click(SI.HIDE_ENV_VALUES_BUTTON)
        for element_name in element_names:
            button_locator = page.define_show_single_value_button_locator(element_name)
            assert page.is_clickable(button_locator), f'Button for {element_name} is not clickable'

    def test_environment_variables_tab_show_hide_each_single_value(self, sys_info_page):
        page = SIP(sys_info_page)
        page.click(SI.ENVIRONMENT_VARIABLES_TAB)
        element_names = page.get_all_element_names(SI.SHOW_ENV_VALUES_BUTTON)
        assert len(element_names) > 0, 'List of environment variables is empty'

        for element_name in element_names:
            show_button = page.define_show_single_value_button_locator(element_name)
            page.click(show_button)
            assert page.is_value_displayed(element_name), f'Value for {element_name} is still hidden'

            hide_button = page.define_hide_single_value_button_locator(element_name)
            page.click(hide_button)
            assert page.is_clickable(show_button), f'Button for {element_name} is not clickable'

    def test_plugins_tab_display_plugins_info(self, sys_info_page):
        page = SIP(sys_info_page)
        page.click(SI.PLUGINS_TAB)
        number_of_plugins = page.number_of_plugins_in_table(SI.PLUGINS_TABLE_BODY)
        assert number_of_plugins > 0

        for i in range(1, number_of_plugins+1):
            name_locator, version_locator, status_locator, plugin_name = page.get_plugin_info(i)
            assert page.is_visible(name_locator), f'Row {i}: Plugin name is not displayed'
            assert page.is_link_clickable(name_locator), f'Row {i}: {plugin_name} is not clickable'
            assert page.is_visible(version_locator), f'Row {i}: {plugin_name} version is not displayed'
            assert page.is_visible(status_locator), f'Row {i}: {plugin_name} status is not displayed'
            assert page.get_element_text(status_locator) in ['true', 'false'], f'Row {i}: {plugin_name} status is not correct'

    def test_memory_usage_tab_select_timespan(self, sys_info_page):
        page = SIP(sys_info_page)
        page.click(SI.MEMORY_USAGE_TAB)
        for option in page.TIMESPAN_OPTIONS:
            page.click(SI.TIMESPAN_DROPDOWN)
            page.select_timespan(option)
            graph = page.get_graph_locator(page.TIMESPAN_OPTIONS.get(option))
            assert page.is_visible(graph), f"Graph for timespan option '{option}' is not displayed, or displayed incorrectly"

    def test_thread_dumps_tab_open_thread_dump_page(self, sys_info_page):
        page = SIP(sys_info_page)
        page.click(SI.THREAD_DUMPS_TAB)
        page.click(SI.THREAD_DUMP_LINK)
        assert page.driver.title == SIP.THREAD_DUMP_TITLE
