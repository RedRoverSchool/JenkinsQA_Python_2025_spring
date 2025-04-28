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

