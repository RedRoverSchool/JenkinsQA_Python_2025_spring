from tests.multi_config.data import description_text, project_name


def test_set_description_for_multi_config_project(multi_config_project_config_page):
    saved_text = multi_config_project_config_page.set_description(description_text, project_name).get_saved_description_text()

    assert saved_text == description_text, f"Expected '{description_text}', but got '{saved_text}'"
