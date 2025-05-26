import allure
import pytest


@pytest.fixture
@allure.title("Prepare: Open Plugins Page")
def plugins(main_page):
    with allure.step("Open Plugins Page"):
        return main_page.go_to_manage_jenkins_page().go_to_plugins_page()
