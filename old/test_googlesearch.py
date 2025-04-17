from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_open_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    driver.quit()+++