import allure
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from utils.test_data import TestUser, TestIngredients


@allure.feature("Основная функциональность")
class TestMainFunctionality:
    @allure.story("Навигация по разделам")
    @allure.title("Переход в конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()
            assert main_page.is_opened()

        with allure.step("Кликнуть на раздел 'Конструктор'"):
            main_page.click_constructor_link()

        with allure.step("Проверить URL"):
            assert "/" in main_page.get_current_url()

    @allure.story("Навигация по разделам")
    @allure.title("Переход в ленту заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Кликнуть на раздел 'Лента заказов'"):
            main_page.click_feed_link()

        with allure.step("Проверить URL"):
            assert "feed" in main_page.get_current_url()

    @allure.story("Работа с конструктором")
    @allure.title("Добавление ингредиента в заказ")
    def test_add_ingredient(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть конструктор"):
            main_page.open()

        with allure.step("Добавить ингредиент"):
            main_page.add_ingredient_to_constructor(TestIngredients.BUN)

        with allure.step("Проверить кнопку оформления"):
            assert main_page.is_element_present(main_page.locators.ORDER_BUTTON)

    @allure.story("Оформление заказа")
    @allure.title("Создание заказа авторизованным пользователем")
    def test_make_order(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        with allure.step("Авторизоваться"):
            login_page.open()
            login_page.login(TestUser.email, TestUser.password)

        with allure.step("Открыть конструктор"):
            main_page.open()

        with allure.step("Добавить ингредиенты"):
            main_page.add_ingredient_to_constructor(TestIngredients.BUN)
            main_page.add_ingredient_to_constructor(TestIngredients.CHEESE)

        with allure.step("Оформить заказ"):
            main_page.click_order_button()

        with allure.step("Проверить модальное окно"):
            assert main_page.is_order_modal_visible()

        with allure.step("Закрыть модальное окно"):
            main_page.close_order_modal()

