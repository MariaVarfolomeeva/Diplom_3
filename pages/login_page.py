from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://stellarburgers.nomoreparties.site/login"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def is_loaded(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Вход']"))
        )

    def login(self, email: str, password: str):
        email_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
        )
        email_input.send_keys(email)

        password_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_input.send_keys(password)

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()
