import allure
import pytest
from tests.manage_jenkins.data import Plugins as DATA


@pytest.fixture
@allure.title("Prepare: Open Plugins Page")
def plugins(main_page):
    with allure.step("Open Plugins Page"):
        return main_page.go_to_manage_jenkins_page().go_to_plugins_page()

@pytest.fixture
@allure.title(f"Prepare: Install \"{DATA.PLUGIN_NAME}\" plugin, open \"Installed plugins\" Page.")
def inst(plugins):
    available_plugins = plugins.go_to_available_plugins_page()
    with allure.step(f"Install \"{DATA.PLUGIN_NAME}\" plugin."):
        available_plugins.type_plugin_name_to_search_field(DATA.PLUGIN_NAME)
    if available_plugins.count_available_plugins() != 0:
        available_plugins.select_plugin_checkbox()
        progress_bar = available_plugins.click_install_button()
        if progress_bar.is_success_loading_plugin_extensions():
            with allure.step("Open \"Installed plugins\" Page."):
                return progress_bar.go_to_installed_plugins_page()
    else:
        with allure.step("Open \"Installed plugins\" Page."):
            return available_plugins.go_to_installed_plugins_page()
