from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_name_with_nonlatin_characters_url(new_item_page):
    new_item_page.find_element(By.XPATH, "/html/body/div[3]/div/div/form/div[2]/div[2]/div[1]/ul/li[1]").click()
    new_item_page.find_element(By.ID, "name").send_keys("狒狒")
    wait5 = WebDriverWait(new_item_page, timeout=5, poll_frequency=0.5)
    wait5.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    assert new_item_page.current_url == "http://localhost:8080/job/%E7%8B%92%E7%8B%92/configure", f"invalid URL: {new_item_page.current_url}"

def test_name_with_with_nonlatin_characters_items(new_item_page):
    new_item_page.find_element(By.XPATH, "/html/body/div[3]/div/div/form/div[2]/div[2]/div[1]/ul/li[1]").click()
    new_item_page.find_element(By.ID, "name").send_keys("狒狒")
    wait5 = WebDriverWait(new_item_page, timeout=5, poll_frequency=0.5)
    wait5.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait5.until(EC.url_to_be("http://localhost:8080/job/%E7%8B%92%E7%8B%92/configure"))
    assert new_item_page.find_element(By.ID, "side-panel").is_displayed(), "Side panel is not displayed after creating a project with non-Latin characters"

def test_name_with_with_nonlatin_characters_buttons(new_item_page):
    new_item_page.find_element(By.XPATH, "/html/body/div[3]/div/div/form/div[2]/div[2]/div[1]/ul/li[1]").click()
    new_item_page.find_element(By.ID, "name").send_keys("狒狒")
    wait5 = WebDriverWait(new_item_page, timeout=5, poll_frequency=0.5)
    wait5.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait5.until(EC.url_to_be("http://localhost:8080/job/%E7%8B%92%E7%8B%92/configure"))
    assert new_item_page.find_element(By.NAME, "Submit").is_enabled(), "Save button (Submit) is not enabled"
    assert new_item_page.find_element(By.NAME, "Apply").is_enabled(), "Apply button is not enabled"
