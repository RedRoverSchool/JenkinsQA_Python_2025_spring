import pytest
from pages.main_page import MainPage

@pytest.mark.parametrize(
    "create_and_build_project_fixture",
    ["remote", "periodically"],
    indirect=True
)
def test_user_can_trigger_build(main_page: MainPage, create_and_build_project_fixture):
    project_name = create_and_build_project_fixture
    builds = main_page.go_to_build_history_page().get_build_list()

    assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    assert builds[0].split("\n")[0] == project_name, f"No build entry found for '{project_name}'"
    assert builds[0].split("\n")[1] == "#1", "Build #1 not found."
