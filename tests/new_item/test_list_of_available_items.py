from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_list_of_available_items(main_page):
    wait = WebDriverWait(main_page, 10)
    list_of_items = ["Freestyle project", "Pipeline", "Multi-configuration project", "Folder", "Multibranch Pipeline", "Organization Folder"]
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tasks"]/div[1]/span/a/span[1]'))).click()
    visible_elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//label/span")))
    actual_elements = [element.text for element in visible_elements]
    assert list_of_items == actual_elements, 'Items do not match'