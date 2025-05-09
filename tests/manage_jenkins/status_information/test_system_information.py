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


def test_environment_variables_tab_show_hide_each_single_value(environment_variables_tab):
    table = environment_variables_tab.get_table_content()
    assert len(table) > 0, "List of environment variables is empty"

    for row in table:
        name = row[0]

        value = environment_variables_tab.click_show_single_value_button(name)
        assert value != SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is still hidden"

        value = environment_variables_tab.click_hide_single_value_button(name)
        assert value == SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is not hidden"


def test_plugins_tab_display_plugins_info(plugins_tab):
    table = plugins_tab.get_table_content()
    assert len(table) > 0, "List of plugins is empty"

    for row in table:
        name = row[0]
        version = row[1]
        enabled_status = row[2]

        assert name, f"Plugin name is empty - {row}"
        assert version, f"Plugin version is empty - {row}"
        assert enabled_status in ["true", "false"], f"Plugin status is incorrect or empty - {row}"


def test_memory_usage_tab_select_timespan(memory_usage_tab):
    for option in SI.TIMESPAN_OPTIONS:
        assert memory_usage_tab.get_graph_for_selected_timespan_option(option), \
            f"Graph for timespan option '{option}' is not displayed, or displayed incorrectly"


def test_thread_dumps_tab_open_thread_dump_page(thread_dumps_tab):
    thread_dump_page = thread_dumps_tab.click_on_thread_dump_page_link()
    assert thread_dump_page.get_title() == "Thread dump [Jenkins]", "Thread dump page title is incorrect"
