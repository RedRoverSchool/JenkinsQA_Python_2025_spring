from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_send_contact_message(driver):
    driver.get("https://automationintesting.online/")
    driver.find_element(By.ID, "name").send_keys("Test User")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "phone").send_keys("1234567890123")
    driver.find_element(By.ID, "subject").send_keys("Test subject")
    (driver.find_element(By.ID, "description").send_keys
     ("This is a testtttttttttttttttttttttttttttttttttttttttttttttttt."))
    button = (WebDriverWait(driver, 3).until(EC.presence_of_element_located
                                             ((By.XPATH, "//button[text()='Submit']"))))
    driver.execute_script("arguments[0].click();", button)

    element = (driver.find_element
    (By.XPATH, '//h3[@class="h4 mb-4" and text()="Thanks for getting in touch "]'))
    assert element.text == "Thanks for getting in touch Test User!", "the text doesn't match"


def test_all_room_images_are_visible(driver):
    driver.get("https://automationintesting.online/")

    images = WebDriverWait(driver, 3).until(
    EC.presence_of_all_elements_located
    ((By.XPATH, '//img[contains(@class, "card-img-top")]')))
    assert images, "No room images found on this page."

    for img in images:
        assert img.is_displayed(), f"not displayed: {img.get_attribute('src')}"

