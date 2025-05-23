import allure
from tests.manage_jenkins.data import SystemInformationData as SI, ManageJenkinsData as MJ


@allure.epic("Manage Jenkins")
@allure.story("Display System Information")
@allure.title("Open System Information Page")
@allure.description("Verify that the System Information page is accessible from the Manage Jenkins page.")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/456", name="TC_10.019.01")
def test_open_system_information_page(manage_jenkins_page):
    sys_info_page = manage_jenkins_page.go_to_system_information_page()
    with allure.step("Check tab headers"):
        assert sys_info_page.get_tabs_bar_headers() == SI.TABS_BAR_HEADERS


@allure.epic("Manage Jenkins")
@allure.story("Display System Information")
@allure.title("System Properties tab - show/hide all values")
@allure.description("Verify that the show/hide all values buttons work properly on the System Properties tab.")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/470", name="TC_10.019.02")
def test_system_properties_tab_show_hide_all_values(system_information_page):
    table = system_information_page.get_table_content()
    with allure.step("Check that the list of system properties is not empty"):
        assert len(table) > 0, "List of system properties is empty"

    system_information_page.click_show_all_values_button()
    table = system_information_page.get_table_content()
    for row in table:
        name, value = row[0], row[1]
        with allure.step(f"Check that the value for {name} is not hidden"):
            assert value != SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is still hidden"

    system_information_page.click_hide_all_values_button()
    table = system_information_page.get_table_content()
    for row in table:
        name, value = row[0], row[1]
        with allure.step(f"Check that the value for {name} is hidden"):
            assert value == SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is not hidden"


@allure.epic("Manage Jenkins")
@allure.story("Display System Information")
@allure.title("System Properties tab - show/hide each single value")
@allure.description("Verify that the individual show/hide value buttons work properly for each name on the System Properties tab.")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/471", name="TC_10.019.03")
def test_system_properties_tab_show_hide_each_single_value(system_information_page):
    table = system_information_page.get_table_content()
    with allure.step("Check that the list of system properties is not empty"):
        assert len(table) > 0, "List of system properties is empty"

    for row in table:
        name = row[0]

        value = system_information_page.click_show_single_value_button(name)
        with allure.step(f"Check that the value for {name} is not hidden"):
            assert value != SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is still hidden"

        value = system_information_page.click_hide_single_value_button(name)
        with allure.step(f"Check that the value for {name} is hidden"):
            assert value == SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is not hidden"


@allure.epic("Manage Jenkins")
@allure.story("Display System Information")
@allure.title("Environment Variables tab - show/hide all values")
@allure.description("Verify that the show/hide all values buttons work properly on the Environment Variables tab.")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/472", name="TC_10.019.04")
def test_environment_variables_tab_show_hide_all_values(environment_variables_tab):
    table = environment_variables_tab.get_table_content()
    with allure.step("Check that the list of environment variables is not empty"):
        assert len(table) > 0, "List of environment variables is empty"

    environment_variables_tab.click_show_all_values_button()
    table = environment_variables_tab.get_table_content()
    for row in table:
        name, value = row[0], row[1]
        with allure.step(f"Check that the value for {name} is not hidden"):
            assert value != SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is still hidden"

    environment_variables_tab.click_hide_all_values_button()
    table = environment_variables_tab.get_table_content()
    for row in table:
        name, value = row[0], row[1]
        with allure.step(f"Check that the value for {name} is hidden"):
            assert value == SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is not hidden"


@allure.epic("Manage Jenkins")
@allure.story("Display System Information")
@allure.title("Environment Variables tab - show/hide each single value")
@allure.description("Verify that the individual show/hide value buttons work properly for each name on the Environment Variables tab.")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/473", name="TC_10.019.05")
def test_environment_variables_tab_show_hide_each_single_value(environment_variables_tab):
    table = environment_variables_tab.get_table_content()
    with allure.step("Check that the list of environment variables is not empty"):
        assert len(table) > 0, "List of environment variables is empty"

    for row in table:
        name = row[0]

        value = environment_variables_tab.click_show_single_value_button(name)
        with allure.step(f"Check that the value for {name} is not hidden"):
            assert value != SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is still hidden"

        value = environment_variables_tab.click_hide_single_value_button(name)
        with allure.step(f"Check that the value for {name} is hidden"):
            assert value == SI.SHOW_SINGLE_VALUE_BUTTON_TEXT, f"{name} - value is not hidden"


@allure.epic("Manage Jenkins")
@allure.story("Display System Information")
@allure.title("Plugins tab - display information about installed plugins")
@allure.description("Verify that information about installed plugins on the Plugins tab is displayed correctly.")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/497", name="TC_10.019.06")
def test_plugins_tab_display_plugins_info(plugins_tab):
    table = plugins_tab.get_table_content()
    with allure.step("Check that the list of plugins is not empty"):
        assert len(table) > 0, "List of plugins is empty"

    for row in table:
        name = row[0]
        version = row[1]
        enabled_status = row[2]

        with allure.step(f"Check that the plugin information is displayed in row #{table.index(row) + 1}"):

            with allure.step(f"Check that the plugin name is displayed: {name}"):
                assert name, f"Plugin name is empty - {row}"

            with allure.step(f"Check that the plugin version is displayed: {version}"):
                assert version, f"Plugin version is empty - {row}"

            with allure.step(f"Check that the plugin status is displayed: {enabled_status}"):
                assert enabled_status in ["true", "false"], f"Plugin status is incorrect or empty - {row}"


@allure.epic("Manage Jenkins")
@allure.story("Display System Information")
@allure.title("Memory Usage tab - display graph according to the selected Timespan")
@allure.description("Verify that the memory usage graph is displayed according to the selected timespan.")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/513", name="TC_10.019.07")
def test_memory_usage_tab_select_timespan(memory_usage_tab):
    for option in MJ.TIMESPAN_OPTIONS:
        with allure.step(f"Check graph link for timespan option '{option}'"):
            assert memory_usage_tab.get_graph_for_selected_timespan_option(option), \
                f"Graph for timespan option '{option}' is not displayed, or displayed incorrectly"


@allure.epic("Manage Jenkins")
@allure.story("Display System Information")
@allure.title("Thread Dumps tab - open Thread Dump page.")
@allure.description("Verify that the page with thread dump information opens from the Thread Dumps tab.")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/519", name="TC_10.019.08")
def test_thread_dumps_tab_open_thread_dump_page(thread_dumps_tab):
    thread_dump_page = thread_dumps_tab.click_on_thread_dump_page_link()
    with allure.step("Check page title"):
        assert thread_dump_page.get_title() == "Thread dump [Jenkins]", "Thread dump page title is incorrect"
