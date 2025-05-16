def test_the_selected_item_type(new_item_page):
        freestyle_element = new_item_page.get_freestyle_element()
        new_item_page.select_freestyle_project()

        selected_items = new_item_page.get_selected_items()

        assert len(selected_items) == 1
        assert selected_items[0] == freestyle_element

        highlighted = new_item_page.get_highlighted_items()
        assert freestyle_element in highlighted
