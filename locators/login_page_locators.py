from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[@class='login-btn']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
