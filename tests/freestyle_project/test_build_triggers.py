import pytest

from tests.freestyle_project.freestyle_data import Freestyle


def test_user_can_trigger_builds_remotely(create_freestyle_project_and_build_remotely):
    builds = create_freestyle_project_and_build_remotely.go_to_build_history_page().get_builds_list()

    assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    assert builds[0].split("\n")[0] == Freestyle.project_name, f"No build entry found for '{Freestyle.project_name}'"
    assert builds[0].split("\n")[1] == "#1", "Build #1 not found."


@pytest.mark.xfail(reason="May fail due to non-reproducible concurrent builds locally.")
def test_user_can_trigger_build_periodically(create_freestyle_project_and_build_periodically):
    builds = create_freestyle_project_and_build_periodically.go_to_build_history_page().get_builds_list()

    assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    assert builds[0].split("\n")[0] == Freestyle.project_name, f"No build entry found for '{Freestyle.project_name}'"
    assert builds[0].split("\n")[1] == "#1", "Build #1 not found."
