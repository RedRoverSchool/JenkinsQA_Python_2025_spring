import allure
import pytest

from pages.new_item_page import NewItemPage
from tests.new_item.data import expected_item_descriptions, expected_item_types


@allure.epic("New Item")
@allure.story("Select an Item type")
@allure.title("Display of project type list")
@allure.description("Verify that the 'New Item' screen displays all available project types.")
@allure.testcase("TC_01.002.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/318", name="Github issue")
def test_display_project_type_list(new_item_page: NewItemPage):
    actual_item_types = new_item_page.get_item_type_names()
    with allure.step("Check item types are match expected"):
        assert actual_item_types == expected_item_types, "Incorrect item types displayed."


@allure.epic("New Item")
@allure.story("Select an Item type")
@allure.title("Display of description each type")
@allure.description("Verify that the 'New Item' screen displays a description of each type of project.")
@allure.testcase("TC_01.002.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/332", name="Github issue")
def test_display_description_of_item_type(new_item_page: NewItemPage):
    actual_names = new_item_page.get_item_type_names()
    actual_descriptions = new_item_page.get_item_type_descriptions()
    with allure.step("Check descriptions match expected"):
        assert actual_descriptions == expected_item_descriptions, "Incorrect item descriptions"
    with allure.step("Check count match"):
        assert len(actual_descriptions) == len(actual_names), "Descriptions count mismatch"


@allure.epic("New Item")
@allure.story("Select an Item type")
@allure.title("Only one project type can be selected")
@allure.description("Verify that only one project type can be selected at a time on the New Item screen.")
@allure.testcase("TC_01.002.03")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/391", name="Github issue")
@pytest.mark.parametrize("first_project", NewItemPage.PROJECT_TYPE_MAP)
def test_only_one_project_can_be_selected(new_item_page, first_project):
    others = [p for p in NewItemPage.PROJECT_TYPE_MAP if p != first_project]
    for second_project in others:
        page = new_item_page
        with allure.step(f"Select the first project type: {first_project}"):
            first_element = page.select_item_and_get_element(first_project)
            assert page.get_active_element() == first_element, f"Expected active element to be '{first_project}'"
        with allure.step(f"Select the second project type: {second_project}"):
            second_element = page.select_item_and_get_element(second_project)
        with allure.step(f"Verify active element is the second selected: {second_project}"):
            assert page.get_active_element() == second_element, f"Expected active element to be '{second_project}'"
            with allure.step("Verify only one project type is selected and highlighted"):
                selected = page.get_selected_items()
                highlighted = page.get_highlighted_items()
                assert len(selected) == 1, "More than one project type is selected"
                assert highlighted == selected, "Highlighted project does not match selected project"
