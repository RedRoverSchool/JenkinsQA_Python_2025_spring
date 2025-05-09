import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def folder(main_page):
    wait = WebDriverWait(main_page, 5)
    folder_name = "Folder_1"

    new_item = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='New Item']/ancestor::a")))
    main_page.execute_script("arguments[0].click();", new_item)
    main_page.find_element(By.CLASS_NAME, "jenkins-input").send_keys(folder_name)
    main_page.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    main_page.find_element(By.ID, "ok-button").click()
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    main_page.find_element(By.XPATH, "//a[text()='Dashboard']").click()
    wait.until(EC.element_to_be_clickable((By.ID, f'job_{folder_name}'))).click()
    main_page.get(f"http://localhost:8080/job/{folder_name}/")

    return wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='This folder is empty']")))


def test_health_metrics_available(main_page, folder):
    wait = WebDriverWait(main_page, 5)

    configure = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Configure']/ancestor::a")))
    configure.click()

    health_metrics = wait.until(EC.visibility_of_element_located((By.ID, "health-metrics")))

    assert health_metrics.is_displayed(), "'Health metrics' not visible"

    is_clickable = EC.element_to_be_clickable((By.ID, "health-metrics"))
    assert is_clickable is not None, "'Health metrics' is not clickable"
