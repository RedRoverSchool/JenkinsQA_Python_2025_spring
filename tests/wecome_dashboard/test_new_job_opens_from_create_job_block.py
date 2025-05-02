def test_new_item_page_opens_after_clicking_create_job_block(new_item_page_opens_after_clicking_create_job_block):
    assert new_item_page_opens_after_clicking_create_job_block.title == "New Item [Jenkins]"


def test_new_item_page_opens_after_clicking_plus_in_create_job_block(
        new_item_page_opens_after_clicking_plus_in_create_job_block):
    assert new_item_page_opens_after_clicking_plus_in_create_job_block.current_url == "http://localhost:8080/newJob"
