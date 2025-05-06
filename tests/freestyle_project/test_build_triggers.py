from tests.freestyle_project.freestyle_data import Freestyle


def test_user_can_trigger_builds_remotely(create_freestyle_project_and_build_remotely, main_page):
    builds = main_page.go_to_build_history_page().get_build_list()

    assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    assert builds[0].split("\n")[0] == Freestyle.project_name, f"No build entry found for '{Freestyle.project_name}'"
    assert builds[0].split("\n")[1] == "#1", "Build #1 not found."