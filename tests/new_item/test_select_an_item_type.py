import allure
import pytest

from pages.new_item_page import NewItemPage


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
