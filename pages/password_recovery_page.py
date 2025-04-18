from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PasswordRecoveryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    EMAIL_INPUT = (By.NAME, "email")
    RECOVERY_BUTTON = (By.XPATH, "//button[@type='submit']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//button[@class='show-password']")
    PASSWORD_INPUT = (By.NAME, "password")

    def open(self):
        self.driver.get("https://example.com/password-recovery")

    def recover_password(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.RECOVERY_BUTTON).click()

    def show_password(self):
        self.driver.find_element(*self.SHOW_PASSWORD_BUTTON).click()

    def get_password_input_style(self):
        return self.driver.find_element(*self.PASSWORD_INPUT).get_attribute("style")
