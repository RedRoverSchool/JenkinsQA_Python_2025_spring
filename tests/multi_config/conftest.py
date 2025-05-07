import pytest
from tests.multi_config.data import project_name


@pytest.fixture
def multi_config_project_config_page(new_item_page):
    return new_item_page.create_new_multi_config_project(project_name)
