from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.freestyle_project.freestyle_data import Freestyle


def test_text_in_description(description_appears):
    assert Freestyle.description_text in description_appears



