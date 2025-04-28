import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from tests.freestyle_project.freestyle_data import Freestyle


def test_exist_environment_section(freestyle):
    environment = freestyle.find_element(By.ID, 'environment')

    assert environment.is_displayed()

@pytest.mark.parametrize('tp_link, tp_wait, tp_expected_text', [
    (Freestyle.tooltip_environment_link[0], Freestyle.tooltip_environment_link_wait[0], Freestyle.tooltip_environment_expected_text[0]),
    (Freestyle.tooltip_environment_link[1], Freestyle.tooltip_environment_link_wait[1], Freestyle.tooltip_environment_expected_text[1])
])
def test_tooltip_environment_items(freestyle, tp_link, tp_wait, tp_expected_text):
    actions = ActionChains(freestyle)
    wait = WebDriverWait(freestyle, 10)
    tooltip_link = freestyle.find_element(By.XPATH, tp_link)
    post_build_actions = freestyle.find_element(By.ID, 'post-build-actions')
    actions.move_to_element(post_build_actions).perform()
    actions.pause(1).move_to_element(tooltip_link).perform()
    tp_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="tippy-content"]'))).text

    assert tp_text == tp_expected_text

def test_create_freestyle_without_environment(freestyle):
    wait = WebDriverWait(freestyle, 10)
    freestyle.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Build Now')))

    assert freestyle.title == f"{Freestyle.project_name} [Jenkins]"
