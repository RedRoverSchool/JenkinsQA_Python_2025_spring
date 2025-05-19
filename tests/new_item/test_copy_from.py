import allure
from pages.new_item_page import NewItemPage
from tests.new_item.data import Copy

@allure.epic("New Item")
@allure.story("Copy from")
@allure.title("Display dynamic dropdown in the \"Copy from\"")
@allure.testcase("TC_01.003.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/396", name="Github issue")
def test_display_dropdown_text(prepare_page_for_copy):
    item_name, expected_result = Copy.FOLDER_NAME_TO_COPY, [Copy.FOLDER_NAME_TO_COPY]

    dropdown_text = prepare_page_for_copy.enter_first_character_in_copy_from(item_name).get_dropdown_text()

    assert dropdown_text, "Dropdown list is empty"
    assert dropdown_text == expected_result, f"Expected text '{expected_result}' NOT FOUND"


@allure.epic("New Item")
@allure.story("Copy from")
@allure.title("Display dynamic dropdown in the \"Copy from\" lowercase character")
@allure.testcase("TC_01.003.11")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/670", name="Github issue")
def test_display_dropdown_text_lowercase(prepare_page_for_copy):
    with allure.step("Getting data"):
        item_name, expected_result = Copy.FOLDER_NAME_TO_COPY.lower(), [Copy.FOLDER_NAME_TO_COPY]

    dropdown_text = prepare_page_for_copy.enter_first_character_in_copy_from(item_name).get_dropdown_text()

    assert dropdown_text, "Dropdown list is empty"
    assert dropdown_text == expected_result, f"Expected text '{expected_result}' NOT FOUND"


@allure.epic("New Item")
@allure.story("Copy from")
@allure.title("Display the dynamic drop-down with the text \"No items\"")
@allure.testcase("TC: 01.003.03")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/441", name="Github issue")
def test_display_dropdown_text_negative(prepare_page_for_copy):
    item_name, expected_result = Copy.NON_EXISTENT_FOLDER_NAME, [Copy.ITEM_NOT_FOUND_MESSAGE]

    dropdown_text = prepare_page_for_copy.enter_first_character_in_copy_from(item_name).get_dropdown_text()

    assert dropdown_text, "Dropdown list is empty"
    assert dropdown_text == expected_result, f"Expected text '{expected_result}' NOT FOUND"


@allure.epic("New Item")
@allure.story("Copy from")
@allure.title("Display an error message \"No such job: item name\"")
@allure.description("Display an error message \"No such job: item name\" when copying an item that does not exist.")
@allure.testcase("TC_01.003.04")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/444", name="Github issue")
def test_error_page_displays_header_and_message(new_item_page: NewItemPage, prepare_page_for_copy):
    error_page = prepare_page_for_copy.go_to_error_page_copy(Copy.COPY_NAME, Copy.NON_EXISTENT_FOLDER_NAME)

    assert error_page.get_header_error() == Copy.HEADER_ERROR, \
        f"Expected header '{Copy.HEADER_ERROR}' NOT FOUND"
    assert error_page.get_message_error() == Copy.MESSAGE_ERROR, \
        f"Expected message '{Copy.MESSAGE_ERROR}' NOT FOUND"
