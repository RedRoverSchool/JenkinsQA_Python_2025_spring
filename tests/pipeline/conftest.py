import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def pipeline_config_page(main_page, config):
    wait5 = WebDriverWait(main_page, 5)
    wait5.until(
        EC.presence_of_element_located((By.XPATH, '//a[@href="/view/all/newJob"]'))
    ).click()
    wait5.until(EC.presence_of_element_located((By.ID, "name"))).send_keys(
        "Pipeline First"
    )
    main_page.find_elements(By.XPATH, '//*[@role="radio"]')[1].click()
    main_page.find_element(By.XPATH, '//*[@type="submit"]').click()
    wait5.until(EC.url_contains("/job/Pipeline%20First/configure"))
    return main_page
