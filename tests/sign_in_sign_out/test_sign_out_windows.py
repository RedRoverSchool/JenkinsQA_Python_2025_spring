from tests.sign_in_sign_out.data import DASHBOARD_TITLE, LOGIN_PAGE_TITLE
from pages.components.components import Header

def test_sign_out_from_all_windows(main_page):
    main_window_handle = main_page.get_current_window_handle()
    new_main_page = main_page.open_dashboard_in_new_window()
    assert new_main_page.get_title() == DASHBOARD_TITLE
    login_page = Header(new_main_page).sign_out()
    assert login_page.is_login_page()
    main_window = new_main_page.switch_to_window(main_window_handle)
    main_window.refresh()
    assert main_window.title == LOGIN_PAGE_TITLE
