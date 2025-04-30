from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_build_steps_availability(freestyle: webdriver.Chrome):
    add_build_step_button = freestyle.find_element(
        By.XPATH,
        "//button[@class='jenkins-button hetero-list-add' and @suffix='builder']",
    )
    add_build_step_button.send_keys(Keys.END)
    add_build_step_button.click()
    wait = WebDriverWait(freestyle, 5)

    build_steps_we = freestyle.find_elements(
        By.XPATH, "//button[@class='jenkins-dropdown__item ']"
    )
    wait.until(EC.element_to_be_clickable(build_steps_we[-1]))
    build_steps_items = {el.text for el in build_steps_we}

    # all 7 asserts are located here purposely because creating separate test for each dropdown's item is redundant
    assert "Execute Windows batch command" in build_steps_items
    assert "Execute shell" in build_steps_items
    assert "Invoke Ant" in build_steps_items
    assert "Invoke Gradle script" in build_steps_items
    assert "Invoke top-level Maven targets" in build_steps_items
    assert "Run with timeout" in build_steps_items
    assert 'Set build status to "pending" on GitHub commit' in build_steps_items
