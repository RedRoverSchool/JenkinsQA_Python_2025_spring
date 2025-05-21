import allure
from tests.freestyle_project.freestyle_data import Freestyle


@allure.epic("Freestyle Project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Enable or Disable the Project")
@allure.testcase("TC_02.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/316", name="Github issue")
def test_enable_disable_switch(freestyle):
    with allure.step("Assert Freestyle Project is Enable"):
        assert freestyle.is_enable().is_displayed()
    with allure.step("Click Disable button"):
        freestyle.switch_to_disable()
    with allure.step("Assert Freestyle Project is Disable"):
        assert freestyle.is_disable().is_displayed()

@allure.epic("Freestyle Project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("A tooltip “Enable or disable the current project” appears")
@allure.testcase("TC_02.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/316", name="Github issue")
def test_tooltip(tooltip):
    with allure.step("assert tooltip is correct"):
        assert tooltip == Freestyle.tooltip_disable

@allure.epic("Freestyle Project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("When Disabled a clear visible warning message")
@allure.testcase("TC_02.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/316", name="Github issue")
def test_disabled_message(disabled_message):
    with allure.step("Assert visible warning message"):
        assert disabled_message == Freestyle.warning_message

@allure.epic("Freestyle Project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("After changing to ”Enable” the Project page get refreshed automatically and the warning message disappear")
@allure.testcase("TC_02.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/316", name="Github issue")
def test_enable_after_disabled(enable_automatically):
    with (allure.step("Assert the warning message disappear")):
        assert enable_automatically[0]
    with allure.step("Assert Freestyle Project is enable"):
        assert enable_automatically[1]
