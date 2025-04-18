import pytest
import logging
from pages.order_feed_page import OrderFeedPage
from utils.api_client import ApiClient
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("driver_setup")
class TestOrderFeed:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_client = ApiClient()

    def test_order_details_popup_opens_on_click(self, driver):
        logger.info("Тест: проверка, что по клику на заказ открывается попап")

        feed = OrderFeedPage(driver)
        feed.open()

        first_order = feed.get_first_order()
        first_order.click()

        assert feed.is_order_popup_displayed(), "Попап с деталями заказа не открылся"

    def test_user_orders_visible_in_feed(self, driver, test_user):
        logger.info("Тест: заказы пользователя видны в ленте заказов")

        self.api_client.create_order_via_api(test_user["access_token"])
        feed = OrderFeedPage(driver)
        feed.open()

        found = feed.find_order_by_user(test_user["email"])
        assert found, "Заказ пользователя не найден в ленте заказов"

    def test_done_counter_increases_after_new_order(self, driver, test_user):
        logger.info("Тест: счётчик 'Выполнено за всё время' увеличивается после нового заказа")

        feed = OrderFeedPage(driver)
        feed.open()

        before = self.api_client.get_total_done_count()
        self.api_client.create_order_via_api(test_user["access_token"])

        feed.refresh()
        after = self.api_client.get_total_done_count()

        assert after > before, f"Счётчик не увеличился: было {before}, стало {after}"

    def test_today_done_counter_increases(self, driver, test_user):
        logger.info("Тест: счётчик 'Выполнено за сегодня' увеличивается после нового заказа")

        feed = OrderFeedPage(driver)
        feed.open()

        count_before = feed.get_done_today_count()
        self.api_client.create_order_via_api(test_user["access_token"])

        feed.refresh()
        count_after = feed.get_done_today_count()

        assert count_after > count_before, f"Сегодняшний счётчик не изменился: {count_before} → {count_after}"

    def test_order_number_appears_in_work(self, driver, test_user):
        logger.info("Тест: номер заказа появляется в разделе 'В работе'")

        order_number = self.api_client.create_order_via_api(test_user["access_token"])
        feed = OrderFeedPage(driver)
        feed.open()

        feed.refresh()

        try:
            in_work = feed.get_orders_in_progress()
            assert any(
                str(order_number) in item.text for item in in_work
            ), f"Заказ #{order_number} не отображается в 'В работе'"
        except NoSuchElementException:
            pytest.fail("Раздел 'В работе' не найден или пуст")
