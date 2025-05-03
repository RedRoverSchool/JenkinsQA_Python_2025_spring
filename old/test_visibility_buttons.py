from selenium import webdriver
from selenium.webdriver.common.by import By


def test_visibility_buttons():
    BASE_URL = "http://uitestingplayground.com/visibility"
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    hide_button = driver.find_element(By.ID, "hideButton")
    zero_width_button = driver.find_element(By.ID, "zeroWidthButton")
    opacity_button = driver.find_element(By.ID, "transparentButton")
    visibility_hidden_button = driver.find_element(By.ID, "invisibleButton")
    display_none_button = driver.find_element(By.ID, "notdisplayedButton")
    offscreen_button = driver.find_element(By.ID, "offscreenButton")

    hide_button.click()
    removed_button_exist = len(driver.find_elements(By.ID, "removedButton"))

    assert removed_button_exist == 0
    assert zero_width_button.value_of_css_property("width") == "0px", "ERROR"
    assert offscreen_button.value_of_css_property("color") == "rgba(255, 255, 255, 1)"
    assert opacity_button.get_attribute("style") == "opacity: 0;"
    assert visibility_hidden_button.get_attribute("style") == "visibility: hidden;"
    assert display_none_button.get_attribute("style") == "display: none;"
    assert offscreen_button.value_of_css_property("position") == "absolute"
    assert offscreen_button.value_of_css_property("top") == "-9999px"
    assert offscreen_button.value_of_css_property("left") == "-9999px"

    driver.quit()
