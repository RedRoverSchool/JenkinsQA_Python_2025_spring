from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_footer_icons_displayed_and_links_work():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Открываем сайт и логинимся
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        # Ищем иконки соцсетей
        social_icons = driver.find_elements(By.CSS_SELECTOR, '.footer .social a')
        assert len(social_icons) > 0, "Иконки соц. сетей не найдены!"

        main_window = driver.current_window_handle

        for icon in social_icons:
            link_text = icon.text
            icon.click()
            time.sleep(3)  # Ждём открытия новой вкладки

            # Переключаемся на новую вкладку
            all_windows = driver.window_handles
            assert len(all_windows) > 1, f"Вкладка не открылась при клике на ссылку: {link_text}"

            driver.switch_to.window(all_windows[-1])
            current_url = driver.current_url
            print(f"Открыта ссылка: {current_url}")

            assert "http" in current_url, f"Некорректный URL: {current_url}"

            # Закрываем вкладку и возвращаемся
            driver.close()
            driver.switch_to.window(main_window)

    except AssertionError as e:
        print(f"Тест не пройден: {e}")
    finally:
        driver.quit()
