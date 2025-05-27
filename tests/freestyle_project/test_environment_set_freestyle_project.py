import allure
import pytest
from tests.freestyle_project.freestyle_data import Freestyle


@allure.epic("Freestyle Project Configuration")
@allure.story("Set up Environment")
@allure.title("The user should be able to select Environment options")
@allure.testcase("TC_02.005.04")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/413", name="Github issue")
@pytest.mark.parametrize('item_name, id_check', Freestyle.environmet_options)
def test_possible_set_environment(freestyle, item_name, id_check):
    with allure.step(f"Select \"{item_name}\" environment options"):
        freestyle.scroll_to_post_build_actions()
        freestyle.click_on_checkbox_environment_options(item_name)
    with allure.step("Apply selected Environment options"):
        freestyle.click_apply_button()
    with allure.step("Assert that Environment options is selected"):
        assert freestyle.is_checkbox_environment_options_selected(id_check)
