import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

@pytest.fixture
def hero(driver):
    driver.get("https://the-internet.herokuapp.com")
    return driver

def test_dropdown(hero):
    hero.find_element(By.XPATH,'//a[@href="/dropdown"]').click()
    hero.find_element(By.ID, 'dropdown').click()
    hero.find_element(By.XPATH, "//option[@value='1']").click()
    assert hero.find_element(By.ID, 'dropdown').get_attribute('value') == '1'

def test_drag_and_drop(hero):
    hero.find_element(By.XPATH, '//a[@href="/drag_and_drop"]').click()
    box1 =hero.find_element(By.ID, 'column-a')
    box2 =hero.find_element(By.ID, 'column-b')
    actions = ActionChains(hero)
    actions.drag_and_drop(box1, box2).perform()
    assert hero.find_element(By.ID, 'column-a').text == 'B'

def test_hovers(hero):
    hero.find_element(By.XPATH, '//a[@href="/hovers"]').click()
    hero.find_element(By.XPATH, "//div[@class='figure'][1]").click()
    assert hero.find_element(By.XPATH, "//h5[contains(text(), 'name: user1')]").is_displayed()

def test_typos(hero):
    hero.find_element(By.XPATH, '//a[@href="/typos"]').click()
    typo = hero.find_element(By.XPATH,".//p[contains(text(), 'Sometimes')]").text
    if typo == "Sometimes you'll see a typo, other times you won,t.":
        print("Grammar mistake is detected")
    else:
        print("Grammar mistake is not detected")

def test_add_remove_elements(hero):
    hero.find_element(By.XPATH, '//a[@href="/add_remove_elements/"]').click()
    hero.find_element(By.XPATH, '//button[@onclick="addElement()"]').click()
    assert hero.find_element(By.XPATH, '//button[@class="added-manually" and @onclick="deleteElement()"]').is_displayed()