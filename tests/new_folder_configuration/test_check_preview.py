from tests.new_folder_configuration.folder_data import FolderNames


def test_check_description_preview(folder_config_page):
    folder_config_page.set_description(FolderNames.item_description)
    folder_config_page.click_preview()
    assert folder_config_page.get_preview_text() == FolderNames.item_description, "Preview doesn't match"

    folder_config_page.hide_preview()
    assert "display: none" in folder_config_page.get_preview_style(), "Preview still visible"
