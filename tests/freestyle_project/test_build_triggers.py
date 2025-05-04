from time import sleep
import logging
from tests.freestyle_project.data import project_name

logger = logging.getLogger(__name__)


def test_user_can_trigger_builds_remotely(main_page, generate_token, get_crumb):
    auth_token = generate_token
    crumb = get_crumb
    username = main_page.get_username()
    password = main_page.get_password()
    server = main_page.get_server()
    build_api = f"http://{username}:{password}@{server}/job/{project_name}/build?token={auth_token}&Jenkins-Crumb={crumb}"

    freestyle_config_page = main_page.go_to_new_item_page().create_freestyle_project(project_name)
    freestyle_project_page = freestyle_config_page.set_trigger_builds_remotely(auth_token, project_name)
    freestyle_project_page.go_to_the_main_page()

    main_page_window = main_page.get_current_window_handle()
    new_window = main_page.switch_to_new_window()

    new_window.get(build_api)
    logger.info(f"Triggered build at: {new_window.current_url}")

    logger.info("Waiting for the build to finish...")
    sleep(10)

    main_page.switch_to(main_page_window)

    build_history_page = main_page.go_to_build_history_page()
    builds = build_history_page.get_build_list()

    assert len(builds) == 1, f"Expected 1 build, found {len(builds)}"
    assert builds[0].split("\n")[0] == project_name, f"No build entry found for project '{project_name}'"
    assert builds[0].split("\n")[1] == "#1", "Build #1 not found."
