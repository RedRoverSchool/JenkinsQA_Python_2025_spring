from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_name_with_only_space_url(new_item_page):
    new_item_page.find_element(By.XPATH, "/html/body/div[3]/div/div/form/div[2]/div[2]/div[1]/ul/li[1]").click()
    new_item_page.find_element(By.ID, "name").send_keys(" ")
    wait5 = WebDriverWait(new_item_page, timeout=5, poll_frequency=0.5)
    wait5.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    assert new_item_page.current_url == "http://localhost:8080/view/all/createItem", f"invalid URL: {new_item_page.current_url}"

def test_name_with_only_space_error_text(new_item_page):
    new_item_page.find_element(By.XPATH, "/html/body/div[3]/div/div/form/div[2]/div[2]/div[1]/ul/li[1]").click()
    new_item_page.find_element(By.ID, "name").send_keys(" ")
    wait5 = WebDriverWait(new_item_page, timeout=5, poll_frequency=0.5)
    wait5.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait5.until(EC.url_to_be("http://localhost:8080/view/all/createItem"))
    assert "Error\nNo name is specified" in new_item_page.find_element(By.ID, "main-panel").text, f"Invalid text found: {new_item_page.find_element(By.ID, 'main-panel').text}"
