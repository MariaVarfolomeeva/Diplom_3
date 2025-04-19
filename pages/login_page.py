from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    PATH = "/login"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    def is_opened(self) -> bool:
        """Проверка, что страница логина загружена"""
        return self.is_element_present(self.locators.HEADER)

    def enter_email(self, email: str) -> None:
        """Ввод email"""
        self.send_keys(self.locators.EMAIL_INPUT, email)

    def enter_password(self, password: str) -> None:
        """Ввод пароля"""
        self.send_keys(self.locators.PASSWORD_INPUT, password)

    def click_submit(self) -> None:
        """Клик по кнопке 'Войти'"""
        self.click_element(self.locators.SUBMIT_BUTTON)

    def login(self, email: str, password: str) -> None:
        """Комплексный метод авторизации"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit()

    def click_forgot_password_link(self) -> None:
        """Переход на страницу восстановления пароля"""
        self.click_element(self.locators.FORGOT_PASSWORD_LINK)

    def click_register_link(self) -> None:
        """Переход на страницу регистрации"""
        self.click_element(self.locators.REGISTER_LINK)

    def get_error_message(self) -> str:
        """Получение текста ошибки"""
        return self.driver.find_element(*self.locators.ERROR_MESSAGE).text

    def is_error_visible(self) -> bool:
        """Проверка наличия ошибки"""
        return self.is_element_present(self.locators.ERROR_MESSAGE)

    def is_redirect_to_register(self) -> bool:
        """Проверяет, что произошел редирект на страницу регистрации"""
        return "register" in self.driver.current_url


