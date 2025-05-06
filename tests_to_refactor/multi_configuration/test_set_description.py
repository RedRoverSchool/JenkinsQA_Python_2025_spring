
def test_set_description_for_multi_config_project(multi_config_project_page):
    description_text = "This is my overview"

    multi_config_project_page.set_description(description_text)
    saved_text = multi_config_project_page.get_saved_description_text()

    assert description_text in saved_text, f"Expected '{description_text}', but got '{saved_text}'"
