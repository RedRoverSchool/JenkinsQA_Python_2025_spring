import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
    
def test_accepted_user_names_are_shown_to_user(sauce):
    user_names_node = sauce.find_element(By.XPATH,"//div[@id='login_credentials']")
    user_names_text = user_names_node.text

    for child in user_names_node.find_elements(By.XPATH,"./*"):
        user_names_text = user_names_text.replace(child.text, "",1).strip()
    
    actual_user_names = user_names_text.splitlines()
    expected_user_names = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]

    assert len(actual_user_names) == len(expected_user_names)
    assert all([a == b for a, b in zip(actual_user_names, expected_user_names)])
