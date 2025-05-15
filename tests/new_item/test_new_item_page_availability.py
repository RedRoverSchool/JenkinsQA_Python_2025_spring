from pages.main_page import MainPage
from tests.new_item.data import title_fragment


def test_new_item_page_is_available(main_page: MainPage):
    main_page.go_to_new_item_page()
    title = main_page.get_title()

    assert title_fragment in title.lower()
