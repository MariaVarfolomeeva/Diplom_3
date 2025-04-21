from selenium.webdriver.common.by import By


class LoginPageLocators:
    HEADER = (By.XPATH, "//h1[text()='Вход']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")

    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Успешный вход')]")
