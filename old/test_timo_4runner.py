import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

'''
https://www.toyota.com/4runner/
'''

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.toyota.com/4runner/")
    # Pause all videos on the page
    driver.execute_script("""
    const videos = document.querySelectorAll('video');
    videos.forEach(video => {
        video.pause();
        video.currentTime = 0;  // Optional: reset to start
    });
    """)
    yield driver
    driver.quit()

def test_build_4runner(driver):

    color = 'Supersonic Red'

    wait = WebDriverWait(driver, 45)
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Decline')]").click()
    except NoSuchElementException:
        pass

    # Step 1: Navigate to 4Runner build page
    driver.find_element(By.XPATH, "//a[@href='/configurator/build/step/model/year/2025/series/4runner']").click()
    driver.find_element(By.XPATH, "//input[@name='zipcode']").send_keys('94002')
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Step 2: Select trim and color
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-grade='TRD Off-Road i-FORCE MAX' and @href]"))).click() 

    swatch = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='vcr-selection-card-inner']//div[@data-code='03U5']")))
    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", swatch)

    # Try regular click first, fallback to JS click if intercepted
    try:
        swatch.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", swatch)

    # Step 3: Confirm changes
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-btntype='add']"))).click()

    # Step 4: Return to main page
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='cta-button-secondary cta button primary']"))).click()

    # Step 5: Validate exterior color
    check_color = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//section/div[@class='detail-wrapper']//span[text()='Supersonic Red ']")
    ))

    assert color in check_color.text