from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

def test_default_login_form_view():
    driver = webdriver.Chrome()  
    wait = WebDriverWait(driver, 5) 
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  

        assert "auth/login" in driver.current_url 

        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username"))) 
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password"))) 
        login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button"))) 
       
        assert username_input.is_displayed()
        assert password_input.is_displayed()
        assert login_button.is_displayed()

        assert username_input.get_attribute("placeholder") == "Username"
        assert password_input.get_attribute("placeholder") == "Password"

        assert username_input.get_attribute("type") == "text"
        assert password_input.get_attribute("type") == "password"
        
        button_color = login_button.value_of_css_property("background-color")

        assert login_button.is_enabled()
        assert login_button.text.strip().lower() == "login"
       
        error_messages = driver.find_elements(By.CSS_SELECTOR, ".oxd-alert-content")
        assert len(error_messages) == 0
        
        login_button.click()
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span"),"Required"))
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span"),"Required"))

        username_error = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span")))
        assert "Required" in username_error.text

        password_error = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span")))
        assert "Required" in password_error.text
        
        expected_color = "rgba(30, 28, 27, 1)"  
        assert button_color == expected_color, f"Цвет кнопки отличается. Ожидался: {expected_color}, найден: {button_color}"
       

    finally:
        driver.quit()

def test_default_footer_LIND():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        linkedin_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='linkedin.com']")))
        original_window = driver.current_window_handle
        
        linkedin_link.click()

        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        assert "linkedin.com" in driver.current_url.lower()

    finally:
        driver.quit()

def test_default_footer_FB():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        facebook_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='facebook.com']")))
        original_window = driver.current_window_handle

        facebook_link.click()

        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        assert "facebook.com" in driver.current_url.lower()

    finally:
        driver.quit()

def test_default_footer_XCOM():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        xcom_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[3]")))
        original_window = driver.current_window_handle

        xcom_link.click()

        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        assert "x.com" in driver.current_url.lower()

    finally:
        driver.quit()

def test_default_footer_youtube():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        youtube_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='youtube.com']")))
        original_window = driver.current_window_handle

        youtube_link.click()

        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        assert "youtube.com" in driver.current_url.lower()

    finally:
        driver.quit()

def test_default_footer_orange():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        orange_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a")))
        original_window = driver.current_window_handle

        orange_link.click()

        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        assert "orangehrm.com" in driver.current_url.lower()

    finally:
        driver.quit()

def test_success_login_redirect():
    user_name = "Admin"
    user_password = "admin123"

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)  
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(user_name)
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(user_password)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".orangehrm-login-button"))).click()

    current_url = driver.current_url
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    driver.quit()

def test_incor_login_redirect():
    user_name = "Odmin"
    user_password = "odmin123"

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)  
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    error_messages = driver.find_elements(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")
    assert len(error_messages) == 0

    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(user_name)
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(user_password)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".orangehrm-login-button"))).click()

    current_url = driver.current_url
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    reg_error = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")))
    assert "Invalid credentials" in reg_error.text

    driver.quit()
