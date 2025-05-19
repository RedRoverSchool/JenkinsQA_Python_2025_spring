from tests.freestyle_project.freestyle_data import Freestyle


def test_add_github_project(freestyle):
    freestyle.check_github_project_option()
    assert freestyle.is_github_project_option_enabled(), "GitHub checkbox isn't selected"

    freestyle.add_project_url(Freestyle.github_project_url)
    freestyle_project_page = freestyle.click_save_button()
    menu_texts = freestyle_project_page.get_menu_items_texts()

    assert any("github" in text.lower() for text in menu_texts), \
        f"GitHub integration not found in menu. Available items: {menu_texts}"
