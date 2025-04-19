from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators

class PasswordRecoveryPage(BasePage):
    PATH = "/forgot-password"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = PasswordRecoveryPageLocators()

    def is_page_opened(self) -> bool:
        """Проверка загрузки страницы по заголовку"""
        return self.is_element_present(self.locators.PAGE_HEADER)

    def submit_recovery_form(self, email: str) -> None:
        """Заполняет и отправляет форму восстановления пароля"""
        self.enter_email(email)
        self.click_recover_button()

    def enter_email(self, email: str) -> None:
        """Вводит email в поле восстановления"""
        self.send_keys(self.locators.EMAIL_INPUT, email)

    def click_recover_button(self) -> None:
        """Нажимает кнопку 'Восстановить'"""
        self.click_element(self.locators.RECOVERY_BUTTON)

    def is_form_submitted(self) -> bool:
        """Проверяет успешную отправку формы (появление сообщения)"""
        return self.is_element_present(self.locators.SUCCESS_MESSAGE)

    def toggle_password_visibility(self) -> None:
        """Переключает видимость пароля (клик на иконку глаза)"""
        self.click_element(self.locators.SHOW_PASSWORD_BUTTON)

    def is_password_visible(self) -> bool:
        """Проверяет, отображается ли пароль (тип поля 'text' вместо 'password')"""
        return "text" in self.driver.find_element(*self.locators.PASSWORD_INPUT).get_attribute("type")

    def is_error_message_displayed(self) -> bool:
        """Проверяет наличие сообщения об ошибке"""
        return self.is_element_present(self.locators.ERROR_MESSAGE)

    def get_error_message(self) -> str:
        """Возвращает текст ошибки"""
        return self.driver.find_element(*self.locators.ERROR_MESSAGE).text

    def click_login_link(self) -> None:
        """Кликает на ссылку 'Войти' для перехода на страницу авторизации"""
        self.click_element(self.locators.LOGIN_LINK)

