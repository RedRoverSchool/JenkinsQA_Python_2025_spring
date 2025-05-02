import pytest

from tests.new_item.data_structs import NewItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import pytest


def test_save_on_folder_configurator(main_page):
    wait = WebDriverWait(main_page, 5)
    test_job = "job" + str(random.randint(1, 100))
    test_folder = "folder" + str(random.randint(1, 100))
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="/view/all/newJob"]'))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#name"))).send_keys(test_job)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder"))).click()

    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait.until(EC.visibility_of_element_located((By.NAME, "_.displayNameOrNull"))).send_keys(test_folder)

    wait.until(EC.presence_of_element_located((By.NAME, "Submit"))).click()

    h1_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#main-panel > h1"))).text.strip()
    wait.until(EC.presence_of_element_located((By.ID, "main-panel")))
    assert h1_element == test_folder, f"Expected name text to be '{test_folder}', but got '{h1_element}'"
