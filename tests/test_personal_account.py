import allure
import pytest
from pages.personal_account_page import PersonalAccountPage
from pages.login_page import LoginPage


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.story("Навигация по личному кабинету")
    @allure.title("Переход в историю заказов")
    def test_navigate_to_order_history(self, authorized_user):
        personal_account = PersonalAccountPage(authorized_user)

        with allure.step("Открыть страницу личного кабинета"):
            personal_account.open()
            assert personal_account.is_profile_page_opened()

        with allure.step("Перейти в историю заказов"):
            personal_account.go_to_order_history()

        with allure.step("Проверить активность раздела"):
            assert personal_account.is_order_history_active()

    @allure.story("Выход из аккаунта")
    @allure.title("Корректный выход из системы")
    def test_logout(self, authorized_user):
        login_page = LoginPage(authorized_user)
        personal_account = PersonalAccountPage(authorized_user)

        with allure.step("Открыть личный кабинет"):
            personal_account.open()

        with allure.step("Выйти из аккаунта"):
            personal_account.logout()

        with allure.step("Проверить редирект на страницу логина"):
            assert login_page.is_opened(), "Не произошел выход из аккаунта"

    @allure.story("История заказов")
    @allure.title("Проверка отображения истории заказов")
    def test_order_history_display(self, authorized_user):
        personal_account = PersonalAccountPage(authorized_user)

        with allure.step("Открыть историю заказов"):
            personal_account.open()
            personal_account.go_to_order_history()

        with allure.step("Проверить наличие заказов"):
            assert personal_account.get_order_history_items_count() > 0, "История заказов пуста"


