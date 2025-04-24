import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from tests.freestyle_project.freestyle_data import Freestyle


def test_scm_to_none(empty_configure):

    assert empty_configure == True

@pytest.mark.parametrize('tp_link, tp_wait, tp_expected_text, count', [
    (Freestyle.tooltip_scm_link[0], Freestyle.tooltip_scm_link_wait[0], Freestyle.tooltip_scm_expected_text[0], 0),
    (Freestyle.tooltip_scm_link[1], Freestyle.tooltip_scm_link_wait[1], Freestyle.tooltip_scm_expected_text[1], 1),
    (Freestyle.tooltip_scm_link[2], Freestyle.tooltip_scm_link_wait[2], Freestyle.tooltip_scm_expected_text[2], 2),
    (Freestyle.tooltip_scm_link[3], Freestyle.tooltip_scm_link_wait[3], Freestyle.tooltip_scm_expected_text[3], 3),
    (Freestyle.tooltip_scm_link[4], Freestyle.tooltip_scm_link_wait[4], Freestyle.tooltip_scm_expected_text[4], 4),
    (Freestyle.tooltip_scm_link[5], Freestyle.tooltip_scm_link_wait[5], Freestyle.tooltip_scm_expected_text[5], 4),
    (Freestyle.tooltip_scm_link[6], Freestyle.tooltip_scm_link_wait[6], Freestyle.tooltip_scm_expected_text[6], 6),
    (Freestyle.tooltip_scm_link[7], Freestyle.tooltip_scm_link_wait[7], Freestyle.tooltip_scm_expected_text[7], 6),
    (Freestyle.tooltip_scm_link[8], Freestyle.tooltip_scm_link_wait[8], Freestyle.tooltip_scm_expected_text[8], 6)
    ])
def test_tooltips(freestyle, tp_link, tp_wait, tp_expected_text, count):
    actions = ActionChains(freestyle)
    wait = WebDriverWait(freestyle, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'general'), 'General'))
    git = freestyle.find_element(By.XPATH, '//label[@for="radio-block-1"]')
    size =freestyle.get_window_size("current")
    to_half = size.get('height')//2
    to_dec = size.get('height')//10
    actions.scroll_by_amount(0, to_half).perform()
    git.click()
    freestyle.find_element(By.XPATH, '//button[@name="Apply"]').click()
    actions.scroll_by_amount(0, to_dec * count).perform()
    if count < 6:
        advanced = freestyle.find_element(By.XPATH, '//div[@class="form-container tr"]//div[@class="jenkins-form-item tr"]//button')
        advanced.click()
        freestyle.find_element(By.XPATH, '//button[@name="Apply"]').click()
    else:
        wait.until(EC.visibility_of_element_located((By.XPATH, tp_link)))
    tooltip_link = freestyle.find_element(By.XPATH, tp_link)
    actions.scroll_to_element(tooltip_link).perform()
    actions.move_to_element(tooltip_link).perform()
    wait.until(EC.presence_of_element_located((By.XPATH, tp_wait)))
    tp_text = freestyle.find_element(By.XPATH, '//div[@class="tippy-content"]').text

    assert tp_text == tp_expected_text