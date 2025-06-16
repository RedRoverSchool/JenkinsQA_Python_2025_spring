import allure
from tests.api.tests_ui.organization_folder.data import project_name, display_name


@allure.epic("Organization folder Configuration")
@allure.story("Change General Settings")
@allure.title("The User can add a Display Name to an existing Organization Folder created by API")
@allure.testcase("TC_07.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/493", name="Github issue")
def test_add_new_display_name(create_organization_folder, main_page):
    org_folder_page = main_page.go_to_the_organization_folder_page(project_name)
    header_text = org_folder_page.get_header_pipeline_page()

    assert header_text == display_name, \
        f'Expected display name "{display_name}" to appear in the header, but got "{header_text}"'
