import allure
from tests.freestyle_project.freestyle_data import Freestyle


@allure.epic("Freestyle Project Configuration")
@allure.story("Project Description")
@allure.title("Add description to the Freestyle Project")
@allure.testcase("TC_02.002.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/366", name="Github issue")
def test_user_can_add_description(can_add_description):
    with allure.step("Assert Freestyle Project has description"):
        assert can_add_description == Freestyle.description_text

@allure.epic("Freestyle Project Configuration")
@allure.story("Project Description")
@allure.title("Description field can remain empty")
@allure.testcase("TC_02.002.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/366", name="Github issue")
def test_empty_description(empty_configure):
    with allure.step("Assert Freestyle Project is created"):
        assert empty_configure == Freestyle.project_name

@allure.epic("Freestyle Project Configuration")
@allure.story("Project Description")
@allure.title("A Preview and Hide preview option is available")
@allure.testcase("TC_02.002.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/366", name="Github issue")
def test_preview_description(preview_hide):
    with allure.step("Assert preview is available"):
        assert preview_hide[0]
    with allure.step("Assert hide is available"):
        assert preview_hide[1]
    # assert is_preview_available and is_hide_available

@allure.epic("Freestyle Project Configuration")
@allure.story("Project Description")
@allure.title("After Saving the Project introduced Description text appears on the Project General page")
@allure.testcase("TC_02.002.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/366", name="Github issue")
def test_description_appears(description_appears):
    with allure.step("Assert Freestyle Project contains description"):
        assert description_appears == Freestyle.description_text