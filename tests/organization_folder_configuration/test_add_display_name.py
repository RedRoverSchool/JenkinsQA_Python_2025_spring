import allure
from tests.organization_folder_configuration.data import project_name, display_name


@allure.epic("Organization folder Configuration")
@allure.story("Change General Settings")
@allure.title("The User can add a Display Name to an existing Organization Folder")
@allure.testcase("TC_07.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/493", name="Github issue")
def test_add_new_display_name(organization_folder_config_page):
    organization_folder_config_page.add_display_name(display_name)
    org_folder_page = organization_folder_config_page.click_save_button(project_name)
    header_text = org_folder_page.get_header_pipeline_page()

    assert header_text == display_name, \
        f'Expected display name "{display_name}" to appear in the header, but got "{header_text}"'
