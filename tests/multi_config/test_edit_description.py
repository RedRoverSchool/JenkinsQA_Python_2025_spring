from tests.multi_config.data import updated_description_text


def test_edit_description_from_project_page(multi_config_project_with_description):
    multi_config_project_with_description.edit_description(updated_description_text)
    text_actual = multi_config_project_with_description.get_saved_description_text()
    assert text_actual == updated_description_text, f"Expected '{updated_description_text}', but got '{text_actual}'"

