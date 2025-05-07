from tests.new_folder_configuration.variables import FolderNames


def test_check_description_preview(folder_config_page):
    item_description = FolderNames.item_description

    folder_config_page.set_description(item_description)
    folder_config_page.click_preview()
    tested_description = folder_config_page.get_preview_text()
    folder_config_page.hide_preview()
    style = folder_config_page.get_preview_style()

    assert tested_description == item_description, "Preview doesn't match"
    assert "display: none" in style, "Preview still visible"
