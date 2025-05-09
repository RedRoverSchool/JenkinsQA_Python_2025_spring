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

    expected_items = {
        "Execute Windows batch command",
        "Execute shell",
        "Invoke Ant",
        "Invoke Gradle script",
        "Invoke top-level Maven targets",
        "Run with timeout",
        'Set build status to "pending" on GitHub commit'
    }

    assert expected_items == build_steps_items
