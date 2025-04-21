import allure
import pytest
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from utils.test_data import TestUser


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.story("Просмотр деталей заказа")
    @allure.title("Открытие деталей заказа из ленты")
    def test_view_order_details(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Открыть ленту заказов"):
            order_feed_page.open()
            assert order_feed_page.is_opened(), "Страница ленты заказов не загрузилась"

        with allure.step("Открыть детали первого заказа"):
            order_feed_page.open_order_details()

        with allure.step("Проверить отображение модального окна"):
            assert order_feed_page.is_order_details_visible(), "Модальное окно с деталями не отобразилось"

        with allure.step("Закрыть модальное окно"):
            order_feed_page.close_order_details()
            assert not order_feed_page.is_order_details_visible(), "Модальное окно не закрылось"

    @allure.story("Статистика заказов")
    @allure.title("Проверка счетчиков заказов")
    def test_orders_counters(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Открыть ленту заказов"):
            order_feed_page.open()

        with allure.step("Получить начальные значения счетчиков"):
            initial_total = order_feed_page.get_total_orders_count()
            initial_today = order_feed_page.get_today_orders_count()

        with allure.step("Проверить, что счетчики отображаются"):
            assert initial_total >= 0, "Неверное значение общего счетчика"
            assert initial_today >= 0, "Неверное значение дневного счетчика"

    @allure.story("Заказы в работе")
    @allure.title("Проверка отображения заказов в работе")
    @pytest.mark.usefixtures("login")
    def test_orders_in_progress(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Открыть ленту заказов"):
            order_feed_page.open()

        with allure.step("Получить список заказов в работе"):
            orders_in_progress = order_feed_page.get_orders_in_progress_numbers()

        with allure.step("Проверить, что список не пуст"):
            assert len(orders_in_progress) > 0, "Нет заказов в работе"

