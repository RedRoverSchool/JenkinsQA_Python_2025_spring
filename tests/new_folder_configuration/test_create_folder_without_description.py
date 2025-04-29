from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_create_folder_without_description(main_page, create_folder):
    wait = WebDriverWait(main_page, 10)
    item_display_name = "Sanity tests"
    create_folder(item_display_name)
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    main_page.find_element(By.CSS_SELECTOR, "[name='Submit']").click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "h4")))
    check_display_name_element = main_page.find_element(By.XPATH, "//*[@id='main-panel']/h1")
    check_display_name = check_display_name_element.text
    check_description_element = main_page.find_element(By.XPATH, "//*[@id='view-message']")
    check_description = check_description_element.text
    assert check_display_name == item_display_name, "Folder name is incorrect"
    assert check_description == "", "Description is present"