from pages.main_page import MainPage
from tests.sign_in_sign_out.data import DASHBOARD_URL, BREADCRUMB_BAR_TEXT, LOGOUT_LINK_TEXT


def test_sign_in_with_valid_credentials(login_page, config):
    main_page: MainPage  = login_page.enter_user_name(config.jenkins.USERNAME).enter_password(config.jenkins.PASSWORD).click_signin_button()
    assert main_page.get_url()  == DASHBOARD_URL
    assert main_page.header.get_breadcrumb_bar_text() == BREADCRUMB_BAR_TEXT
    assert main_page.header.get_logout_link_text() == LOGOUT_LINK_TEXT




