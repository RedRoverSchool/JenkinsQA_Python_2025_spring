import allure
from tests.sign_in_sign_out.data import DASHBOARD_TITLE, LOGIN_PAGE_TITLE
from pages.components.components import Header


@allure.epic("Sign in/out")
@allure.story("Sign out")
@allure.title("""If multiple Jenkins windows were previously opened in the browser,
after signing out, attempting to access any Jenkins page redirects the user to the login page.""")
@allure.testcase("TC_08.002.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/697", name="Github issue")
def test_sign_out_from_all_windows(main_page):
    with allure.step("Save handle of the current \"first window\""):
        main_window_handle = main_page.get_current_window_handle()
    with allure.step("Open dashboard in new \"second window\""):
        new_main_page = main_page.open_dashboard_in_new_window()
        assert new_main_page.get_title() == DASHBOARD_TITLE
    with allure.step("Doing Sign out on the \"second window\""):
        login_page = Header(new_main_page).sign_out()
    with allure.step("Assert that \"second windows\" is \"Login page\" window"):
        assert login_page.is_login_page()
    with allure.step("Come back to the first \"window\""):
        main_window = new_main_page.switch_to_window(main_window_handle)
        main_window.refresh()
    with allure.step("Assert that \"first windows\" is \"Login page\" window"):
        assert main_window.title == LOGIN_PAGE_TITLE
