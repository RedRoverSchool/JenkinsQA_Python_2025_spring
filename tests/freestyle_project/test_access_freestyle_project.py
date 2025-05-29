from pages.freestyle_project_page import FreestyleProjectPage
from tests.freestyle_project.freestyle_data import Freestyle as DATA


def test_access_freestyle_project(access):
    assert access.get_project_row_data(DATA.project_name)[2] == DATA.project_name
    freestyle_page: FreestyleProjectPage = access.click_on_project(DATA.project_name)
    assert freestyle_page.get_h1_value() == DATA.project_name
