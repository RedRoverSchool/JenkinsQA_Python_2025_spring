from pages.new_item_page import NewItemPage


def test_only_one_project_can_be_selected(new_item_page: NewItemPage):
    page = new_item_page
    pipeline_item = page.get_pipeline_element()
    page.click_element(pipeline_item)
    assert page.get_active_element() == pipeline_item

    freestyle_item = page.get_freestyle_element()
    page.click_element(freestyle_item)
    assert page.get_active_element() == freestyle_item

    selected_items = page.get_selected_items()
    highlighted_items = page.get_highlighted_items()
    assert len(selected_items) == 1
    assert highlighted_items == selected_items
