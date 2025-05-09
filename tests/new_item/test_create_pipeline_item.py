from tests.new_item.data import new_pipeline_name


def test_create_pipeline_item(new_item_page):
    pipelines = new_item_page.create_new_pipeline(new_pipeline_name).go_to_the_main_page().get_item_list()
    assert pipelines == [new_pipeline_name], f"Pipeline '{new_pipeline_name}' NOT FOUND"
