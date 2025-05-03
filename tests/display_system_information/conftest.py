import pytest
from tests.display_system_information.system_information_page import (
    SystemInformationPage as SI,
)


@pytest.fixture(scope="function")
def sys_info_page(main_page):
    main_page.get(main_page.current_url + SI.ENDPOINT_URL)
    return main_page
