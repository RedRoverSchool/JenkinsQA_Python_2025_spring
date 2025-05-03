from tests.freestyle_project.freestyle_data import Freestyle


def test_user_can_add_description(can_add_description):
    assert can_add_description == Freestyle.description_text


def test_empty_description(empty_configure):
    assert empty_configure


def test_preview_description(preview_hide):
    is_preview_available = preview_hide[0]
    is_hide_available = preview_hide[1]

    assert is_preview_available and is_hide_available


def test_description_appears(description_appears):
    assert description_appears == Freestyle.description_text
