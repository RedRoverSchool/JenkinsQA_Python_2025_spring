import pytest
from tests.multi_config.data import project_name
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture
def multi_config_project_config_page(new_item_page):
    return new_item_page.create_new_multi_config_project(project_name)


@pytest.fixture
def multi_config_project_with_description(new_item_page):
    from tests.multi_config.data import project_name, description_text
    config_page = new_item_page.create_new_multi_config_project(project_name)
    return config_page.set_description(description_text, project_name)
