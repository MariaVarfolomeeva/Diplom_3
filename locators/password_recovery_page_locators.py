from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    RECOVERY_BUTTON = (By.XPATH, "//button[@type='submit']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//button[@class='show-password']")
    PASSWORD_INPUT = (By.NAME, "password")
