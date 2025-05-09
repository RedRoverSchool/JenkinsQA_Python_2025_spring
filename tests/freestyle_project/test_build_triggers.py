from pages.main_page import MainPage


def test_user_can_trigger_builds_remotely(main_page: MainPage, create_freestyle_project_and_build_remotely):
    project_name = create_freestyle_project_and_build_remotely
    builds = main_page.go_to_build_history_page().get_build_list()

    assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    assert builds[0].split("\n")[0] == project_name, f"No build entry found for '{project_name}'"
    assert builds[0].split("\n")[1] == "#1", "Build #1 not found."

def test_user_can_trigger_builds_periodically(main_page: MainPage, create_freestyle_project_and_build_periodically):
    project_name = create_freestyle_project_and_build_periodically
    builds = main_page.go_to_build_history_page().get_build_list()

    assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    assert builds[0].split("\n")[0] == project_name, f"No build entry found for '{project_name}'"
    assert builds[0].split("\n")[1] == "#1", "Build #1 not found."
