from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_helping_icon(main_page, create_folder):
    wait = WebDriverWait(main_page, 10)
    item_name = "Folder one"
    create_folder(item_name)
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '(//*[@class="jenkins-help-button"])[1]')
        )
    ).click()
    element = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="main-panel"]/form/div[1]/div[2]/div/div[4]/div/div[1]')
        )
    )
    text = element.text
    main_page.find_element(By.XPATH, '(//*[@class="jenkins-help-button"])[1]').click()
    expected_text = "If set, the optional display name is shown for the project throughout the Jenkins web GUI."

    assert expected_text in text, "The text is not matched"
    assert not element.is_displayed(), "Help message still visible"
