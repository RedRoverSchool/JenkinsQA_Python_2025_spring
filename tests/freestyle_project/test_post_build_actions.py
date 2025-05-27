import allure
from tests.freestyle_project.freestyle_data import Freestyle


@allure.epic("Freestyle Project Configuration")
@allure.story("Post-Build Actions")
@allure.title("A \"Post-Build Actions\" section should be available during project setup.")
@allure.testcase("TC_02.007.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/671", name="Github issue")
def test_post_build_actions_is_available(freestyle):
    with allure.step("Scrool to the Post-Build section"):
        freestyle.scroll_to_bottom_screen()
    with allure.step("Assert that Post-Build Actions is displayed"):
        assert freestyle.get_post_build_actions_element().is_displayed()
    
@allure.epic("Freestyle Project Configuration")
@allure.story("Post-Build Actions")
@allure.title("The user should be able to add one or more post-build actions")
@allure.testcase("TC_02.007.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/671", name="Github issue")
def test_add_post_build_actions(freestyle):
    with allure.step("Get list current Post-Build Actions"):
        freestyle.scroll_to_bottom_screen()
        freestyle.click_add_post_build_actions()
    with allure.step("Assert that current list Post-Build Actions is equal to extected list"):
        assert freestyle.get_items_post_build_actions() == Freestyle.ITEMS_POST_BUILD_ACTION