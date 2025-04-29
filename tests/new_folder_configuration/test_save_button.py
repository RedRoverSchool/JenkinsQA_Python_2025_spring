from tests.new_item.data_structs import NewItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time

def test_save_on_folder_configurator(main_page):
    wait = WebDriverWait(main_page, 5)
    testjob = "job" + str(random.randint(1,100))
    testfolder = "folder" + str(random.randint(1,100))
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="/view/all/newJob"]'))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#name"))).send_keys(testjob)
    main_page.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    main_page.find_element(By.ID, "ok-button").click()
    wait.until(EC.visibility_of_element_located((By.NAME, "_.displayNameOrNull"))).send_keys(testfolder)
    main_page.find_element(By.NAME, "Submit").click()
    h1_element = main_page.find_element(By.CSS_SELECTOR, "h1").text.strip()
    foldername = main_page.find_element(By.ID, "main-panel")
    assert h1_element == testfolder, f"Expected name text to be '{testfolder}', but got '{h1_element}'"