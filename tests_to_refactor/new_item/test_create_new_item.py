from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait


new_folder_name = 'Test_Folder'
DEFAULT_TIMEOUT = 10


def wait_for(driver, by, selector, timeout=DEFAULT_TIMEOUT):
    return wait(driver, timeout).until(
        EC.visibility_of_element_located((by, selector))
    )


def wait_for_clickable(driver, by, selector, timeout=DEFAULT_TIMEOUT):
    return wait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector))
    )


