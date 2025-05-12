from tests.pipeline.pipeline_data import description_text


def test_add_description_to_pipeline(pipeline_config_page):
    pipeline_page = pipeline_config_page.add_description(description_text).click_save_button()
    assert pipeline_page.is_description_element_displayed, "Description is not visible"

    desc_element_text = pipeline_page.get_description_text()
    assert desc_element_text == description_text, \
        f"Expected description '{description_text}', but got '{desc_element_text}'"