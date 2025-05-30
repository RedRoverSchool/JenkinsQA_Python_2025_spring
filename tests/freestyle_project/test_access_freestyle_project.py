import allure

from pages.freestyle_project_page import FreestyleProjectPage
from tests.freestyle_project.freestyle_data import Freestyle as DATA


@allure.epic("Freestyle Project Management")
@allure.story("Access to the Project from the Dashboard")
@allure.title("Access to the Freestyle Project from the Dashboard")
@allure.testcase("TC_18.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/829", name="Github issue")
def test_access_freestyle_project(access):
    with allure.step("Assert that on Main Page exist created Freestyle Project"):
        assert access.get_project_row_data(DATA.project_name)[2] == DATA.project_name
    with allure.step(f"Click on \"{DATA.project_name}\" on Main Page"):
        freestyle_page: FreestyleProjectPage = access.click_on_project(DATA.project_name)
    with allure.step("Assert that opened Freestyle Project Page"):
        assert freestyle_page.get_h1_value() == DATA.project_name

@allure.epic("Freestyle Project Management")
@allure.story("Access to the Project options from dropdown menu")
@allure.title("Get set items dropdown menu")
@allure.testcase("TC_18.002.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/839", name="Github issue")
def test_access_from_dropdown(access):
    access.hover_to_dropdown_project()
    elems = access.get_list_dropdown_project_elems()
    items = access.get_list_dropdown_project_items(elems)
    with allure.step("Assert that set items dropdown menu eqeal to expexcted result."):
        assert items == DATA.ITEMS_DROPDOWN_PROJECT
