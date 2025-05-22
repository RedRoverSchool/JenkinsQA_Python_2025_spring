import allure
import pytest
from tests.freestyle_project.freestyle_data import Freestyle


@allure.epic("Freestyle Project Configuration")
@allure.story("Configure SCM")
@allure.title("If no SCM is selected, the project should still be creatable")
@allure.testcase("TC_02.003.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/370", name="Github issue")
def test_scm_to_none(empty_configure):
    with allure.step("Assert If no SCM is selected, the project should still be creatable"):
        assert empty_configure

@allure.epic("Freestyle Project Configuration")
@allure.story("Configure SCM")
@allure.title("Tooltips for all SCM options should be available")
@allure.testcase("TC_02.003.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/370", name="Github issue")
@pytest.mark.parametrize('tp_link, tp_expected_text, count', Freestyle.tooltip_scm)
def test_tooltips(freestyle, tp_link, tp_expected_text, count):
    with allure.step("Show all options for SCM"):
        freestyle.scroll_to_trigger()
        freestyle.click_git()
        freestyle.click_apply_button()
        freestyle.scroll_down(count)
        if 3 < count < 6:
            freestyle.click_git_advanced()
            freestyle.click_apply_button()
#allure.dynamic.parameter("tp_expected_text", tp_expected_text)
    with allure.step(f"Assert current tooltip equal to \"{tp_expected_text}\""):
        assert freestyle.get_tooltip(tp_link) == tp_expected_text
