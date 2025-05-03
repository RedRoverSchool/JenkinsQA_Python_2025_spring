from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_display_project_type_list(main_page):
    wait5 = WebDriverWait(main_page, 5)
    main_page.find_element(By.XPATH, "//a[@href ='/view/all/newJob']").click()
    wait5.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='items']")))
    expected_types_list = [
        "Freestyle project",
        "Pipeline",
        "Multi-configuration project",
        "Folder",
        "Multibranch Pipeline",
        "Organization Folder",
    ]
    actual_types_list = [
        element.text for element in main_page.find_elements(By.XPATH, "//label/span")
    ]

    assert actual_types_list == expected_types_list


def test_display_description_of_type_item(main_page):
    wait5 = WebDriverWait(main_page, 5)
    main_page.find_element(By.XPATH, "//a[@href ='/view/all/newJob']").click()
    wait5.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='desc']")))
    project_types = main_page.find_elements(By.XPATH, "//label/span")
    descriptions = main_page.find_elements(By.XPATH, "//div[@class='desc']")
    valid_descriptions = [desc for desc in descriptions if desc.text.strip()]

    assert len(valid_descriptions) == len(project_types), (
        "Количество описаний не совпадает с количеством типов проектов!"
    )


def test_only_one_project_can_be_selected(main_page):
    wait5 = WebDriverWait(main_page, 5)
    main_page.find_element(By.XPATH, "//a[@href ='/view/all/newJob']").click()
    wait5.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='items']")))
    pipeline_item = main_page.find_element(
        By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob"
    )
    freestyle_item = main_page.find_element(
        By.CLASS_NAME, "hudson_model_FreeStyleProject"
    )
    pipeline_item.click()
    wait5.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".org_jenkinsci_plugins_workflow_job_WorkflowJob.active")
        )
    )
    freestyle_item.click()
    wait5.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".hudson_model_FreeStyleProject.active")
        )
    )
    selected_items = main_page.find_elements(By.XPATH, "//li[@aria-checked='true']")
    highlighted_items = main_page.find_elements(By.CLASS_NAME, "active")

    assert (
        len(highlighted_items) == len(selected_items) == 1
        and "Freestyle project" in highlighted_items[0].text
    )
