from tests.display_system_information.base_methods import BaseMethods
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
