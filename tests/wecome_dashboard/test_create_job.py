import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

project_name = "Project 2"


@pytest.mark.parametrize(
    "project",
    [
        "Freestyle project",
        "Pipeline",
        "Multi-configuration project",
        "Folder",
        "Multibranch Pipeline",
        "Organization Folder",
    ],
)
def test_create_job_from_create_job_block(
    new_item_page_opens_after_clicking_create_job_block, config, project
):
    wait5 = WebDriverWait(new_item_page_opens_after_clicking_create_job_block, 5)
    wait5.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(
        project_name
    )

    new_item_page_opens_after_clicking_create_job_block.execute_script(
        "window.scrollBy(0, 500);"
    )
    new_item_page_opens_after_clicking_create_job_block.find_element(
        By.XPATH, f"//*[text() = '{project}']"
    ).click()
    new_item_page_opens_after_clicking_create_job_block.find_element(
        By.ID, "ok-button"
    ).click()

    wait5.until(EC.visibility_of_element_located((By.NAME, "Submit"))).click()

    wait5.until(EC.url_changes((config.jenkins.base_url + f"/job/{project_name}/")))

    if project == "Multi-configuration project":
        expected_project_name = f"Project {project_name}"
        actual_project_name = wait5.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[text() = 'Project {project_name}']")
            )
        ).text
    else:
        expected_project_name = project_name
        actual_project_name = wait5.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[text() = '{project_name}']")
            )
        ).text

    assert actual_project_name == expected_project_name, (
        f"The expected project job '{project_name}' not found"
    )
