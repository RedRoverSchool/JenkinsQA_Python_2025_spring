from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_description_to_pipeline(pipeline_config_page):
    text_for_description = "test description"
    text_box = WebDriverWait(pipeline_config_page, 10).until(
        EC.visibility_of_element_located((By.NAME, 'description')))
    text_box.send_keys(text_for_description)
    pipeline_config_page.find_element(By.NAME, "Submit").click()
    desc_element = WebDriverWait(pipeline_config_page, 10).until(
        EC.visibility_of_element_located((By.ID, "description")))
    assert desc_element.is_displayed(), f"Description element is not visible"
    assert desc_element.text == text_for_description, \
        f"Expected description '{text_for_description}', but got '{desc_element.text}'"


