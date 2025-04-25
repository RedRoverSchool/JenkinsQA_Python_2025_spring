from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.freestyle_project.freestyle_data import Freestyle

text = Freestyle.description_text

def test_freestyle(freestyle,main_page):
    wait5 = WebDriverWait(main_page, 5)
    main_page.find_element(By.NAME, "description").send_keys(text)
    wait5.until(EC.visibility_of_element_located((By.NAME, "Submit"))).click()

def test_text_in_description(description_page):
    container = description_page.find_element(By.CSS_SELECTOR, "#description")
    assert text in container



