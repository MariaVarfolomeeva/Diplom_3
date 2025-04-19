import allure
import pytest
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from utils.test_data import TestData


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.story("Переход на страницу восстановления пароля")
    def test_can_open_password_recovery_page(self, driver):
        """
        Тест проверяет корректность перехода на страницу восстановления пароля
        со страницы логина
        """
        with allure.step("Открываем страницу логина"):
            login_page = LoginPage(driver)
            login_page.open()

        with allure.step("Кликаем на ссылку 'Забыли пароль?'"):
            login_page.click_forgot_password_link()

        with allure.step("Проверяем открытие страницы восстановления"):
            recovery_page = PasswordRecoveryPage(driver)
            assert recovery_page.is_page_opened(), (
                f"Ожидался переход на страницу восстановления пароля, "
                f"но открыт URL: {driver.current_url}"
            )

    @allure.story("Восстановление пароля с валидным email")
    def test_submit_recovery_form(self, driver):
        """
        Тест проверяет отправку формы восстановления пароля
        с валидным email
        """
        with allure.step("Открываем страницу восстановления пароля"):
            recovery_page = PasswordRecoveryPage(driver)
            recovery_page.open()

        with allure.step("Заполняем email и отправляем форму"):
            recovery_page.submit_recovery_form(TestData.RECOVERY_EMAIL)

        with allure.step("Проверяем сообщение об успешной отправке"):
            assert recovery_page.is_form_submitted(), (
                "Ожидалось подтверждение отправки ссылки для восстановления"
            )

    @allure.story("Переключение видимости пароля")
    def test_password_visibility_toggle(self, driver):
        """
        Тест проверяет работу кнопки показа/скрытия пароля
        """
        with allure.step("Открываем страницу восстановления пароля"):
            recovery_page = PasswordRecoveryPage(driver)
            recovery_page.open()

        with allure.step("Проверяем, что пароль скрыт по умолчанию"):
            assert not recovery_page.is_password_visible(), (
                "Пароль должен быть скрыт по умолчанию"
            )

        with allure.step("Нажимаем иконку показа пароля"):
            recovery_page.toggle_password_visibility()

        with allure.step("Проверяем, что пароль стал видимым"):
            assert recovery_page.is_password_visible(), (
                "Пароль должен отображаться после нажатия иконки"
            )

        with allure.step("Нажимаем иконку скрытия пароля"):
            recovery_page.toggle_password_visibility()

        with allure.step("Проверяем, что пароль снова скрыт"):
            assert not recovery_page.is_password_visible(), (
                "Пароль должен скрыться после повторного нажатия"
            )

    @allure.story("Восстановление с несуществующим email")
    def test_recovery_with_invalid_email(self, driver):
        """
        Тест проверяет обработку несуществующего email
        при восстановлении пароля
        """
        with allure.step("Открываем страницу восстановления пароля"):
            recovery_page = PasswordRecoveryPage(driver)
            recovery_page.open()

        with allure.step("Вводим несуществующий email"):
            recovery_page.submit_recovery_form(TestData.UNREGISTERED_EMAIL)

        with allure.step("Проверяем сообщение об ошибке"):
            assert recovery_page.is_error_message_displayed(), (
                "Ожидалось сообщение об ошибке для несуществующего email"
            )
            error_text = recovery_page.get_error_message().lower()
            assert "не найден" in error_text or "не существует" in error_text, (
                f"Неожиданное сообщение об ошибке: {error_text}"
            )

    @allure.story("Переход на страницу входа")
    def test_login_link_from_recovery_page(self, driver):
        """
        Тест проверяет работу ссылки для перехода
        на страницу входа со страницы восстановления пароля
        """
        with allure.step("Открываем страницу восстановления пароля"):
            recovery_page = PasswordRecoveryPage(driver)
            recovery_page.open()

        with allure.step("Кликаем на ссылку 'Войти'"):
            recovery_page.click_login_link()

        with allure.step("Проверяем переход на страницу входа"):
            login_page = LoginPage(driver)
            assert login_page.is_page_opened(), (
                "Ожидался переход на страницу входа после клика по ссылке"
            )

