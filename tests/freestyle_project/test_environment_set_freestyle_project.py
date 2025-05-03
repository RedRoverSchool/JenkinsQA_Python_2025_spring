import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


@pytest.mark.parametrize(
    "item_name, id_check",
    [
        ("Delete workspace before build starts", "cb18"),
        ("Use secret text(s) or file(s)", "cb19"),
        ("Add timestamps to the Console Output", "cb20"),
        ("Inspect build log for published build scans", "cb21"),
        ("Terminate a build if it's stuck", "cb22"),
        ("With Ant", "cb23"),
    ],
)
def test_possible_set_environment(freestyle, item_name, id_check):
    actions = ActionChains(freestyle)
    post_build_actions = freestyle.find_element(By.ID, "post-build-actions")
    actions.move_to_element(post_build_actions).perform()
    checkbox = freestyle.find_element(
        By.XPATH,
        f'//label[text()="{item_name}"]/ancestor::span[@class="jenkins-checkbox"]',
    )
    checkbox.click()
    freestyle.find_element(By.XPATH, '//button[@name="Apply"]').click()
    inb = freestyle.find_element(By.XPATH, f'//input[@id="{id_check}"]')

    assert inb.is_selected()
