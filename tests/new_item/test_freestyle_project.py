from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_create_freestyle_project_1(main_page):
    wait = WebDriverWait(main_page, 5)
    project_name = "Freestyle Project"

    main_page.find_element(By.LINK_TEXT, "Create a job").click()
    main_page.find_element(By.ID, "name").send_keys(project_name)
    main_page.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    main_page.find_element(By.ID, "ok-button").click()
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    main_page.find_element(By.ID, "jenkins-home-link").click()
    wait.until(EC.visibility_of_element_located((By.ID, "projectstatus")))
    new_project_name = main_page.find_element(By.CLASS_NAME, "inside").text
    amount_of_projects = len(main_page.find_elements(By.CSS_SELECTOR, "#projectstatus>tbody>tr"))

    assert amount_of_projects == 1
    assert new_project_name == project_name

def test_create_freestyle_project_2(main_page):
    wait = WebDriverWait(main_page, 5)
    project_name = "Freestyle Project"

    main_page.find_element(By.LINK_TEXT, "Create a job").click()
    main_page.find_element(By.ID, "name").send_keys(project_name)
    main_page.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    main_page.find_element(By.ID, "ok-button").click()
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    main_page.find_element(By.ID, "jenkins-home-link").click()
    wait.until(EC.visibility_of_element_located((By.ID, "projectstatus")))
    new_project_name = main_page.find_element(By.CLASS_NAME, "inside").text
    amount_of_projects = len(main_page.find_elements(By.CSS_SELECTOR, "#projectstatus>tbody>tr"))

    assert amount_of_projects == 1
    assert new_project_name == project_name