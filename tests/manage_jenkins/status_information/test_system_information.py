from pages.manage_jenkins.status_information.data import SystemInformationData as SI


def test_open_system_information_page(manage_jenkins_page):
    sys_info_page = manage_jenkins_page.go_to_sys_info_page()
    assert sys_info_page.get_tabs_bar_headers() == SI.TABS_BAR_HEADERS
