from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_github_project(freestyle):
    github_checkbox = WebDriverWait(freestyle, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="githubProject"]')))
    freestyle.execute_script("arguments[0].click();", github_checkbox)

    assert github_checkbox.is_selected(), "GitHub checkbox isn't selected"

    project_url_field = WebDriverWait(freestyle, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[contains(text(),"Project url")]//following-sibling::div/input')))
    project_url_field.send_keys("https://github.com/RedRoverSchool/OpenWeatherPython_06")
    freestyle.find_element(By.CSS_SELECTOR, '[name="Submit"]').click()
    menu_items = WebDriverWait(freestyle, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="task "]')))
    menu_texts = [item.text for item in menu_items]

    assert any("github" in text.lower() for text in menu_texts), \
        f"GitHub integration not found in menu. Available items: {menu_texts}"
