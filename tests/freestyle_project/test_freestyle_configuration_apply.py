from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.freestyle_project.freestyle_data import Freestyle
import time

def test_apply_button(freestyle,config):
    wait = WebDriverWait(freestyle, 10)
    wait.until(EC.presence_of_element_located((By.NAME, 'description'))).send_keys("description-test")
    freestyle.find_element(By.NAME,"Apply").click()
    saved_bar = wait.until(EC.presence_of_element_located((By.ID, 'notification-bar')))
    description = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="json"]')))
    assert "Saved" in saved_bar.text
    assert "configure" in freestyle.current_url
    assert "description-test" in description.get_attribute("value")


