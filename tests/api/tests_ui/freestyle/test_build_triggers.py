import allure


@allure.epic("Freestyle Project Configuration")
@allure.story("Build Triggers")
@allure.title("User is able to configure and trigger periodic builds as scheduled.")
@allure.description("A User can enable the \"Build periodically trigger\" in a Freestyle project "
                    "and that the build runs according to the specified schedule.")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/643", "TC_02.004.002")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/643", name="Github issue")
def test_user_can_trigger_build_periodically(create_freestyle_project_scheduled_every_minute_by_api, main_page):
    project_name, timeout = create_freestyle_project_scheduled_every_minute_by_api

    builds = main_page\
        .go_to_freestyle_project_page(project_name)\
        .wait_for_build_execution(timeout)\
        .header.go_to_the_main_page()\
        .go_to_build_history_page()\
        .get_builds_list()

    with allure.step("Attach screenshot before asserting number of builds."):
        screenshot = main_page.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="builds_list_screenshot", attachment_type=allure.attachment_type.PNG)
    with allure.step("Assert that only one build is displayed in the list."):
        assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    with allure.step(f"Assert that the project name of the displayed build is \"{project_name}\"."):
        assert builds[0].split("\n")[0] == project_name, f"No build entry found for '{project_name}'"
    with allure.step("Assert that the build has number \"#1\"."):
        assert builds[0].split("\n")[1] == "#1", "Build #1 not found."


def test_freestyle_project_ui_fields_match_api_json(create_freestyle_scheduled_project_by_xml_via_api, main_page):
    project_name, json_data = create_freestyle_scheduled_project_by_xml_via_api
    page = main_page.go_to_freestyle_project_page(project_name)
    assert project_name in json_data.get("url")
    assert page.get_h1_value() == json_data.get("displayName")
    assert page.get_description() == json_data.get("description")

    builds_ui = page.header.go_to_the_main_page() \
        .go_to_build_history_page() \
        .get_builds_list()

    first_build_ui_number = builds_ui[0].split("\n")[1]
    first_build_json_number = f"#{json_data['builds'][0]['number']}"

    assert first_build_ui_number == first_build_json_number == "#1"
