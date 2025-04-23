def test_copy_from_option_exists(main_page,new_item):
    new_item.create_freestyle_project()
    new_item.copy_from_option_exist()