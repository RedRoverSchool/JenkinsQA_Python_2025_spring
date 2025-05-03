import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_empty_description(main_page):
    wait = WebDriverWait(main_page, 5)
    test_job = "job" + str(random.randint(1, 100))
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//a[@href="/view/all/newJob"]'))
    ).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#name"))).send_keys(
        test_job
    )
    main_page.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    main_page.find_element(By.ID, "ok-button").click()
    wait.until(EC.presence_of_element_located((By.NAME, "Submit"))).click()
    description_element = wait.until(
        EC.presence_of_element_located((By.ID, "description"))
    )
    description_text = description_element.text.strip()
    assert description_text == "", (
        f"Description is not empty! Got: '{description_text}'"
    )
