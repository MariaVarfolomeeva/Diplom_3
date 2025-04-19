import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.test_data import TestUser


@allure.feature("Авторизация")
class TestLogin:
    @allure.story("Успешный логин")
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        with allure.step("Открыть страницу логина"):
            login_page.open()
            assert login_page.is_opened(), "Страница логина не загрузилась"

        with allure.step("Ввести валидные данные"):
            login_page.login(TestUser.EMAIL, TestUser.PASSWORD)

        with allure.step("Проверить редирект на главную"):
            assert main_page.is_opened(), "Авторизация не удалась"

    @allure.story("Логин с неверным паролем")
    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)

        with allure.step("Ввести неверный пароль"):
            login_page.open()
            login_page.login(TestUser.EMAIL, "wrong_password")

        with allure.step("Проверить сообщение об ошибке"):
            assert login_page.is_error_visible(), "Ошибка не отобразилась"
            assert "неверный пароль" in login_page.get_error_message().lower()

    @allure.story("Переход на страницу восстановления пароля")
    def test_go_to_password_recovery(self, driver):
        login_page = LoginPage(driver)

        with allure.step("Кликнуть на 'Забыли пароль?'"):
            login_page.open()
            login_page.click_forgot_password_link()

        with allure.step("Проверить редирект"):
            assert "forgot-password" in driver.current_url

    @allure.story("Переход на страницу регистрации")
    @allure.story("Переход на страницу регистрации")
    def test_go_to_register_page(self, driver):
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу логина"):
            login_page.open()

        with allure.step("Кликнуть на ссылку 'Зарегистрироваться'"):
            login_page.click_register_link()

        with allure.step("Проверить редирект"):
            assert login_page.is_redirect_to_register(), "Редирект на регистрацию не выполнен"

