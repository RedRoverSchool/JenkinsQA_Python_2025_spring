import allure
import pytest

from tests.freestyle_project.freestyle_data import Freestyle


@allure.epic("Freestyle Project Configuration")
@allure.story("Build Triggers")
@allure.title("User is able to trigger builds remotely with a valid Authentication Token.")
@allure.description("Enabling the Builds remotely trigger of a Freestyle Project allows the user "
                    "to remotely trigger builds via the Jenkins API using a valid Authentication Token.")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/504", name="TC_02.004.003")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/504", name="Github issue")
def test_user_can_trigger_builds_remotely(create_freestyle_project_and_build_remotely):
    builds = create_freestyle_project_and_build_remotely.go_to_build_history_page().get_builds_list()

    with allure.step("Assert that only one build is displayed in the list."):
        assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    with allure.step(f"Assert that the project name of the displayed build is \"{Freestyle.project_name}\"."):
        assert builds[0].split("\n")[0] == Freestyle.project_name, f"No build entry found for '{Freestyle.project_name}'"
    with allure.step("Assert that the build has number \"#1\"."):
        assert builds[0].split("\n")[1] == "#1", "Build #1 not found."


@allure.epic("Freestyle Project Configuration")
@allure.story("Build Triggers")
@allure.title("User is able to configure and trigger periodic builds as scheduled.")
@allure.description("A User can enable the \"Build periodically trigger\" in a Freestyle project "
                    "and that the build runs according to the specified schedule.")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/643", "TC_02.004.002")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/643", name="Github issue")
@pytest.mark.xfail(reason="May fail due to non-reproducible concurrent builds locally.")
def test_user_can_trigger_build_periodically(create_freestyle_project_and_build_periodically):
    builds = create_freestyle_project_and_build_periodically.go_to_build_history_page().get_builds_list()

    with allure.step("Assert that only one build is displayed in the list."):
        assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    with allure.step(f"Assert that the project name of the displayed build is \"{Freestyle.project_name}\"."):
        assert builds[0].split("\n")[0] == Freestyle.project_name, f"No build entry found for '{Freestyle.project_name}'"
    with allure.step("Assert that the build has number \"#1\"."):
        assert builds[0].split("\n")[1] == "#1", "Build #1 not found."
