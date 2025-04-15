from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Настройки браузера(test)
options = Options()
options.add_argument("--start-maximized")  # Открыть окно в полном размере
# options.add_argument("--headless")      # Раскомментируй, если хочешь headless режим

# Установка и запуск драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Тестовая загрузка страницы
driver.get("https://www.yahoo.com")
print("Заголовок:", driver.title)

driver.quit()
+++

