from tests.manage_jenkins.status_information.data import SystemInformationData as SI


def test_open_system_information_page(manage_jenkins_page):
    sys_info_page = manage_jenkins_page.go_to_system_information_page()
    assert sys_info_page.get_tabs_bar_headers() == SI.TABS_BAR_HEADERS


def test_system_properties_tab_show_hide_all_values(system_information_page):
    table = system_information_page.get_table_content()
    assert len(table) > 0, "List of system properties is empty"

    system_information_page.click_show_all_values_button()
    table = system_information_page.get_table_content()
    for row in table:
        name, value = row[0], row[1]
        assert value != SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is still hidden"

    system_information_page.click_hide_all_values_button()
    table = system_information_page.get_table_content()
    for row in table:
        name, value = row[0], row[1]
        assert value == SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is not hidden"


def test_system_properties_tab_show_hide_each_single_value(system_information_page):
    table = system_information_page.get_table_content()
    assert len(table) > 0, "List of system properties is empty"

    for row in table:
        name = row[0]

        value = system_information_page.click_show_single_value_button(name)
        assert value != SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is still hidden"

        value = system_information_page.click_hide_single_value_button(name)
        assert value == SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is not hidden"


def test_environment_variables_tab_show_hide_all_values(environment_variables_tab):
    table = environment_variables_tab.get_table_content()
    assert len(table) > 0, "List of environment variables is empty"

    environment_variables_tab.click_show_all_values_button()
    table = environment_variables_tab.get_table_content()
    for row in table:
        name, value = row[0], row[1]
        assert value != SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is still hidden"

    environment_variables_tab.click_hide_all_values_button()
    table = environment_variables_tab.get_table_content()
    for row in table:
        name, value = row[0], row[1]
        assert value == SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is not hidden"
