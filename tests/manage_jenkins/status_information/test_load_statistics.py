import allure
from tests.manage_jenkins.data import ManageJenkinsData as MJ


@allure.epic("Manage Jenkins")
@allure.story("Load Statistics")
@allure.title("Open Load Statistics page")
@allure.description("Verify that the Load statistics page is accessible from the Manage Jenkins page.")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/721", name="TC_10.022.01")
def test_open_load_statistics_page(manage_jenkins_page):
    load_stat_page = manage_jenkins_page.go_to_load_statistics_page()
    with allure.step("Check page title"):
        assert load_stat_page.get_title() == "Jenkins Load Statistics [Jenkins]", "Load statistics page title is incorrect"


@allure.epic("Manage Jenkins")
@allure.story("Load Statistics")
@allure.title("Display graph according to the selected Timespan")
@allure.description("Verify that the load statistics graph is displayed according to the selected timespan.")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/722", name="TC_10.022.02")
def test_load_statistics_page_select_timespan(load_statistics_page):
    for option in MJ.TIMESPAN_OPTIONS:
        with allure.step(f"Check graph link for timespan option '{option}'"):
            assert load_statistics_page.get_graph_for_selected_timespan_option(option), \
                f"Graph for timespan option '{option}' is not displayed, or displayed incorrectly"
