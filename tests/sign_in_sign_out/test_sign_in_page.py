from pages.login_page import LoginPage
from tests.sign_in_sign_out.data import sign_in_form_header


def test_signin_fields(login_page: LoginPage):
    actual_sign_in_form_header = login_page.get_sign_in_form_header()

    assert actual_sign_in_form_header == sign_in_form_header, f"expected: '{sign_in_form_header}', actual: '{actual_sign_in_form_header}'"
    assert login_page.login_field_is_displayed(), "Username field is not displayed"
    assert login_page.password_field_is_displayed(), "Password field is not displayed"
    assert login_page.keep_me_signed_checkbox_is_displayed(), "Keep me signed checkbox is not displayed"
