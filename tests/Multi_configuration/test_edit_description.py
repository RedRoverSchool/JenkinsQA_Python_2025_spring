import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.skip(reason="Тест временно отключён для стабилизации окружения")
def test_edit_description_from_project_page(multi_config_project_with_description_page):
    wait = WebDriverWait(multi_config_project_with_description_page, 10)
    updated_text = "Updated project summary"

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="description-link"]'))).click()
    desc_input = wait.until(EC.presence_of_element_located((By.NAME, "description")))
    desc_input.clear()
    desc_input.send_keys(updated_text)
    multi_config_project_with_description_page.find_element(By.NAME, "Submit").click()
    for _ in range(2):
        try:
            desc_element = wait.until(EC.presence_of_element_located((By.ID, "description")))
            assert updated_text in desc_element.text, f"Expected '{updated_text}', but got '{desc_element.text}'"
            break
        except Exception:
            time.sleep(1)  # микропаузу на случай лагов
    else:
        raise AssertionError("Description was not updated properly after 2 tries.")