from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait

from conftest import main_page

new_folder_name = 'Test_Folder'
DEFAULT_TIMEOUT = 10


def wait_for(driver, by, selector, timeout=DEFAULT_TIMEOUT):
    return wait(driver, timeout).until(
        EC.visibility_of_element_located((by, selector))
    )


def test_check_create_new_item(new_item_page,jenkins_reset):
    wait_for(new_item_page, By.CSS_SELECTOR, '#name').send_keys(new_folder_name)
    folder_option = wait_for(new_item_page, By.CSS_SELECTOR, '[class*="cloudbees_hudson_plugins_folder"]')
    folder_option.click()
    button_ok = wait_for(new_item_page, By.CSS_SELECTOR, '#ok-button')
    button_ok.click()
    button_save = wait_for(new_item_page, By.CSS_SELECTOR, '[name=Submit]')
    button_save.click()
    wait_for(new_item_page, By.CSS_SELECTOR, "#jenkins-name-icon").click()

    assert new_item_page.find_elements(By.XPATH,
                                   f"//table[@id='projectstatus']//tbody//tr[contains(., '{new_folder_name}')]"), \
        f"Folder '{new_folder_name}' NOT FOUND"
