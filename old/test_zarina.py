from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_dropdown():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.find_element(By.ID, 'dropdown').click()
    driver.find_element(By.XPATH, "//option[@value='1']").click()
    assert driver.find_element(By.ID, 'dropdown').get_attribute('value') == '1'
    driver.quit()

def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    box1 =driver.find_element(By.ID, 'column-a')
    box2 =driver.find_element(By.ID, 'column-b')
    actions = ActionChains(driver)
    actions.drag_and_drop(box1, box2).perform()
    assert driver.find_element(By.ID, 'column-a').text == 'B'
    driver.quit()

def test_hovers():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/hovers")
    driver.find_element(By.XPATH, "//div[@class='figure'][1]").click()
    assert driver.find_element(By.XPATH, "//h5[contains(text(), 'name: user1')]").is_displayed()
    driver.quit()

def test_typos():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/typos")
    typo = driver.find_element(By.XPATH,".//p[contains(text(), 'Sometimes')]").text
    if typo == "Sometimes you'll see a typo, other times you won,t.":
        print("Grammar mistake is detected")
    else:
        print("Grammar mistake is not detected")
    driver.quit()

def test_dropdowns():
    driver = webdriver.Chrome()
    driver.get("https://letcode.in/dropdowns")
    driver.find_element(By.ID, 'fruits').click()
    apple = driver.find_element(By.XPATH, "//*[@id='fruits']/option[2]")
    assert apple.text == 'Apple'
    driver.quit()
