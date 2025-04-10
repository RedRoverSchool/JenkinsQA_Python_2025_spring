from selenium import webdriver #webdriver — это основной интерфейс для работы с браузером (например, Chrome) в Selenium.
from selenium.webdriver.common.by import By #By — класс, который помогает указать метод нахождения элементов на странице (например, по имени, CSS-селектору, XPath и т. д.).
from selenium.webdriver.support.ui import WebDriverWait #WebDriverWait — класс для явных ожиданий. Мы используем его для того, чтобы ожидать появления элемента на странице до выполнения дальнейших действий.
from selenium.webdriver.support import expected_conditions as EC #expected_conditions (EC) — модуль с предустановленными ожиданиями, такими как проверка присутствия элемента, видимости и другие условия.

def test_default_login_form_view():
    driver = webdriver.Chrome()  #Мы создаем объект driver, который запускает браузер Chrome. Этот объект управляет браузером для автоматизации тестов.
    wait = WebDriverWait(driver, 5) #Мы создаем объект wait, который будет ожидать появления элемента на странице в течение 10 секунд. Если элемент не появляется за это время, тест завершится с ошибкой.
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  #Открывается веб-страница для авторизации на сайте "OrangeHRM" с использованием метода get(). Мы передаем URL страницы логина.

        # Проверка URL
        assert "auth/login" in driver.current_url #С помощью driver.current_url получаем текущий URL страницы.Мы проверяем, что в URL присутствует подстрока "auth/login". Это необходимо для удостоверения, что мы находимся на нужной странице.

        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username"))) #Поле ввода для имени пользователя с атрибутом name="username".
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password"))) #Поле ввода для пароля с атрибутом name="password"
        login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button"))) #Кнопка логина, которая определяется с помощью CSS-селектора .orangehrm-login-button.
        #Мы используем wait.until() с условием EC.presence_of_element_located(), чтобы дождаться, пока элементы появятся на странице.
        # Проверка, что элементы отображаются
        #Здесь мы проверяем, что все элементы формы (поля ввода и кнопка) действительно отображаются на странице. Метод .is_displayed() возвращает True, если элемент видим на экране.
        assert username_input.is_displayed()
        assert password_input.is_displayed()
        assert login_button.is_displayed()

        # Проверка плейсхолдеров
        #Мы проверяем, что у полей ввода правильные плейсхолдеры (тексты, которые отображаются в пустых полях).
        #Для этого используется метод .get_attribute("placeholder"), который извлекает значение атрибута placeholder элемента.
        assert username_input.get_attribute("placeholder") == "Username"
        assert password_input.get_attribute("placeholder") == "Password"

        # Проверка атрибута type
        #Мы проверяем, что атрибут type для поля имени пользователя равен "text", а для пароля — "password". Это важно для обеспечения безопасности формы (например, для скрытия пароля).
        assert username_input.get_attribute("type") == "text"
        assert password_input.get_attribute("type") == "password"
        # Получаем цвет кнопки
        button_color = login_button.value_of_css_property("background-color")

        # Проверка кнопки
        #Мы проверяем, что кнопка логина доступна для клика (метод .is_enabled()).
        #Затем проверяем, что текст на кнопке равен "login", игнорируя пробелы и регистр (метод .strip().lower()).
        assert login_button.is_enabled()
        assert login_button.text.strip().lower() == "login"

        # Проверка, что не появляется ошибка сразу
        #Мы ищем все элементы с классом .oxd-alert-content, которые могут содержать сообщения об ошибках (например, неверный логин/пароль).
        #Убедимся, что таких сообщений нет на странице до того, как мы отправим форму.
        error_messages = driver.find_elements(By.CSS_SELECTOR, ".oxd-alert-content")
        assert len(error_messages) == 0

        # После клика на кнопку логина
        #Теперь мы кликаем по кнопке логина, что отправляет форму.
        login_button.click()
        #После клика на кнопку логина мы ждем появления ошибок для обоих полей (имя пользователя и пароль), если они не заполнены.
        #Мы используем EC.visibility_of_element_located, чтобы дождаться, пока элементы с ошибками станут видимыми.
        #После того как элемент появляется, мы проверяем, что текст ошибки содержит строку "Required", что означает, что поле обязательно для заполнения.
        wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span"),
            "Required"
        ))
        wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span"),
            "Required"
        ))

        # Проверка появления ошибки для поля username
        username_error = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span")
        ))
        assert "Required" in username_error.text

        # Проверка появления ошибки для поля password
        password_error = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span")
        ))
        assert "Required" in password_error.text
        # Пример, как можно проверить цвет, если ожидается конкретный
        expected_color = "rgba(30, 28, 27, 1)"  # Пример ожидаемого цвета (можно заменить на нужный цвет)
        assert button_color == expected_color, f"Цвет кнопки отличается. Ожидался: {expected_color}, найден: {button_color}"
        #После выполнения всех действий (независимо от того, прошел тест или нет) мы закрываем браузер с помощью driver.quit(). Это важный шаг для освобождения ресурсов.

    finally:
        driver.quit()

def test_default_footer_LIND():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Прокручиваем до футера
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ищем ссылку на LinkedIn (пример)
        linkedin_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='linkedin.com']")))
        original_window = driver.current_window_handle

        # Кликаем по ссылке
        linkedin_link.click()

        # Ждём открытия нового окна
        wait.until(EC.number_of_windows_to_be(2))

        # Переключаемся на новое окно
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # Проверяем URL новой вкладки
        assert "linkedin.com" in driver.current_url.lower()

    finally:
        driver.quit()

def test_default_footer_FB():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Прокручиваем до футера
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ищем ссылку на Facebook
        facebook_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='facebook.com']")))
        original_window = driver.current_window_handle

        # Кликаем по ссылке
        facebook_link.click()

        # Ждём открытия нового окна
        wait.until(EC.number_of_windows_to_be(2))

        # Переключаемся на новое окно
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # Проверяем URL новой вкладки
        assert "facebook.com" in driver.current_url.lower()

    finally:
        driver.quit()

def test_default_footer_XCOM():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Прокручиваем до футера
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ищем ссылку на xcom (пример)
        xcom_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[3]")))
        original_window = driver.current_window_handle

        # Кликаем по ссылке
        xcom_link.click()

        # Ждём открытия нового окна
        wait.until(EC.number_of_windows_to_be(2))

        # Переключаемся на новое окно
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # Проверяем URL новой вкладки
        assert "x.com" in driver.current_url.lower()

    finally:
        driver.quit()

def test_default_footer_youtube():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Прокручиваем до футера
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ищем ссылку на YouTube (пример)
        youtube_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='youtube.com']")))
        original_window = driver.current_window_handle

        # Кликаем по ссылке
        youtube_link.click()

        # Ждём открытия нового окна
        wait.until(EC.number_of_windows_to_be(2))

        # Переключаемся на новое окно
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # Проверяем URL новой вкладки
        assert "youtube.com" in driver.current_url.lower()

    finally:
        driver.quit()

def test_default_footer_orange():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Прокручиваем до футера
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ищем ссылку на YouTube (пример)
        orange_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a")))
        original_window = driver.current_window_handle

        # Кликаем по ссылке
        orange_link.click()

        # Ждём открытия нового окна
        wait.until(EC.number_of_windows_to_be(2))

        # Переключаемся на новое окно
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # Проверяем URL новой вкладки
        assert "orangehrm.com" in driver.current_url.lower()

    finally:
        driver.quit()

def test_success_login_redirect():
    user_name = "Admin"
    user_password = "admin123"

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)  # немного увеличим ожидание на всякий
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(user_name)
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(user_password)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".orangehrm-login-button"))).click()

    # # ждём редирект или появления дашборда
    # wait.until(EC.url_contains("/dashboard/index"))

    current_url = driver.current_url
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    driver.quit()

def test_incor_login_redirect():
    user_name = "Odmin"
    user_password = "odmin123"

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)  # немного увеличим ожидание на всякий
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    error_messages = driver.find_elements(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")
    assert len(error_messages) == 0

    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(user_name)
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(user_password)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".orangehrm-login-button"))).click()

    # # ждём редирект или появления дашборда
    # wait.until(EC.url_contains("/dashboard/index"))

    current_url = driver.current_url
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    reg_error = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")))
    assert "Invalid credentials" in reg_error.text

    driver.quit()