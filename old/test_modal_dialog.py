import pytest
from core.settings import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def config():
    return Config.load()

@pytest.fixture(scope="function")
def driver(config):
    match config.browser.NAME:
        case "chrome":
            from selenium.webdriver.chrome.options import Options
            options = Options()
            options.page_load_strategy="none"
            for argument in config.browser.OPTIONS_CHROME.split(';'):
                options.add_argument(argument)
            driver = webdriver.Chrome(options=options)
        case "edge":
            from selenium.webdriver.edge.options import Options
            options = Options()
            for argument in config.browser.OPTIONS_EDGE.split(';'):
                options.add_argument(argument)
            driver = webdriver.Edge(options=options)
        case _:
            raise RuntimeError(f"Browser {config.browser.NAME} is not supported.")
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.fixture
def modal(driver):
    driver.get("https://demoqa.com/modal-dialogs")
    return driver

@pytest.mark.parametrize(
    "body_text, id_show, id_button, title",
    [
        ("This is a small modal", "showSmallModal", "closeSmallModal", "Small Modal"),
        ("Lorem Ipsum is simply dummy text of the printing and typesetting industry", "showLargeModal",
         "closeLargeModal", "Large Modal")
    ]
)
def test_modal_dialog(modal, body_text, id_show, id_button, title):
    waiter5 = WebDriverWait(modal, 5)
    waiter5.until(EC.visibility_of_element_located((By.ID, id_show)))
    modal.find_element(By.ID, id_show).click()
    waiter5.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]')))
    modal.switch_to.active_element.find_element(By.XPATH, '//div[@role="dialog"]')
    m_title = modal.find_element(By.CLASS_NAME, "modal-title").text
    m_body = modal.find_element(By.CLASS_NAME, "modal-body").text.split(".")
    m_button = modal.find_element(By.ID, id_button)
    m_button_text = m_button.text
    m_button.click()

    assert m_title == title
    assert m_body[0] == body_text
    assert m_button_text == "Close"