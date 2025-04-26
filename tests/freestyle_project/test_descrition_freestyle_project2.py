from tests.freestyle_project.freestyle_data import Freestyle

def test_text_in_description(description_appears):
    assert Freestyle.description_text in description_appears