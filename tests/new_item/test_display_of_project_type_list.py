from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_display_project_type_list(main_page):
    wait5 = WebDriverWait(main_page, 5)
    main_page.find_element(By.XPATH, "//a[@href ='/view/all/newJob']").click()
    wait5.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='items']")))
    expected_types_list = ["Freestyle project", "Pipeline", "Multi-configuration project",
                           "Folder", "Multibranch Pipeline", "Organization Folder"]
    actual_types_list = [element.text for element in main_page.find_elements(By.XPATH, "//label/span")]

    assert actual_types_list == expected_types_list
