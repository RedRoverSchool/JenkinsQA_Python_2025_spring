from tests.freestyle_project.freestyle_data import Freestyle

def test_post_build_actions_is_available(freestyle):
    freestyle.scroll_to_bottom_screen()
    assert freestyle.get_port_build_actions_element().is_displayed()
    
def test_add_post_build_actions(freestyle):
    freestyle.scroll_to_bottom_screen()
    freestyle.click_add_post_build_actions()
    assert freestyle.get_items_post_build_actions() == Freestyle.ITEMS_POST_BUILD_ACTION