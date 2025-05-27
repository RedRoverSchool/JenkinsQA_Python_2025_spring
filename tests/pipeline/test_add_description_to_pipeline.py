import allure
from tests.pipeline.pipeline_data import description_text, pipeline_project_name


@allure.epic("Pipeline Configuration")
@allure.story("Project Description")
@allure.title("Add Description to Pipeline")
@allure.testcase("TC_03.002.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/368", name="Github issue")
def test_add_description_to_pipeline(pipeline_config_page):
    with allure.step("Enter pipeline description text to the Description text box and click \"Save\" button"):
        pipeline_page = pipeline_config_page.add_description(description_text).click_save_button(pipeline_project_name)
    with allure.step("Verify if description is visible"):
        assert pipeline_page.is_description_element_displayed, "Description is not visible"
    with allure.step("Get description text from the Pipeline General page"):
        desc_element_text = pipeline_page.get_description_text()
    with allure.step("Verify that after saving correct description text is displayed on the Pipeline General page"):
        assert desc_element_text == description_text, \
        f"Expected description '{description_text}', but got '{desc_element_text}'"
