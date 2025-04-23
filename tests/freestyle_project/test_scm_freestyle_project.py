import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from tests.freestyle_project.freestyle_data import Freestyle


def test_scm_to_none(empty_configure):

    assert empty_configure == True

@pytest.mark.xfail(strick=False)
@pytest.mark.parametrize('tp_link, tp_wait, tp_expected_text, scrool_down', [
    (Freestyle.tooltip_scm_link[0], Freestyle.tooltip_scm_link_wait[0], Freestyle.tooltip_scm_expected_text[0], False),
    (Freestyle.tooltip_scm_link[1], Freestyle.tooltip_scm_link_wait[1], Freestyle.tooltip_scm_expected_text[1], False),
    (Freestyle.tooltip_scm_link[2], Freestyle.tooltip_scm_link_wait[2], Freestyle.tooltip_scm_expected_text[2], False),
    (Freestyle.tooltip_scm_link[3], Freestyle.tooltip_scm_link_wait[3], Freestyle.tooltip_scm_expected_text[3], False),
    (Freestyle.tooltip_scm_link[4], Freestyle.tooltip_scm_link_wait[4], Freestyle.tooltip_scm_expected_text[4], False),
    (Freestyle.tooltip_scm_link[5], Freestyle.tooltip_scm_link_wait[5], Freestyle.tooltip_scm_expected_text[5], True),
    (Freestyle.tooltip_scm_link[6], Freestyle.tooltip_scm_link_wait[6], Freestyle.tooltip_scm_expected_text[6], True),
    (Freestyle.tooltip_scm_link[7], Freestyle.tooltip_scm_link_wait[7], Freestyle.tooltip_scm_expected_text[7], True),
    (Freestyle.tooltip_scm_link[8], Freestyle.tooltip_scm_link_wait[8], Freestyle.tooltip_scm_expected_text[8], True)
    ])
def test_tooltips(freestyle, tp_link, tp_wait, tp_expected_text, scrool_down):
    actions = ActionChains(freestyle)
    wait = WebDriverWait(freestyle, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'general'), 'General'))
    actions.scroll_by_amount(0, 100).perform()
    freestyle.find_element(By.XPATH, '//label[@for="radio-block-1"]').click()
    actions.scroll_by_amount(0, 500).perform()
    if scrool_down:
        actions.scroll_by_amount(0,500).perform()
    advanced = freestyle.find_element(By.XPATH, '//div[@class="form-container tr"]//div[@class="jenkins-form-item tr"]//button')
    advanced.click()
    tooltip_link = freestyle.find_element(By.XPATH, tp_link)
    actions.move_to_element(tooltip_link).perform()
    wait.until(EC.presence_of_element_located((By.XPATH, tp_wait)))
    tp_text = freestyle.find_element(By.XPATH, '//div[@class="tippy-content"]').text

    assert tp_text == tp_expected_text