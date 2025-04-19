from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    PAGE_HEADER = (By.XPATH, "//h1[text()='Восстановление пароля']")
    EMAIL_INPUT = (By.NAME, "email")
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_INPUT = (By.NAME, "password")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Ссылка для восстановления отправлена')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
