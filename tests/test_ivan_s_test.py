def test_login(login_page):
    assert login_page.title == "Sign in [Jenkins]"


def test_main_page(main_page):
    assert main_page.title == "Dashboard [Jenkins]"

