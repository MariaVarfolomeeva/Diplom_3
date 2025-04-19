from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    PATH = "/feed"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()

    def is_opened(self) -> bool:
        """Проверка загрузки страницы"""
        return self.is_element_present(self.locators.TOTAL_ORDERS_COUNT)

    def open_order_details(self, order_index: int = 0) -> None:
        """Открыть детали заказа по индексу"""
        orders = self.driver.find_elements(*self.locators.ORDER_ITEM)
        orders[order_index].click()

    def is_order_details_visible(self) -> bool:
        """Проверка видимости модального окна с деталями заказа"""
        return self.is_element_present(self.locators.ORDER_DETAILS_MODAL)

    def close_order_details(self) -> None:
        """Закрыть модальное окно с деталями заказа"""
        self.click_element(self.locators.CLOSE_MODAL_BUTTON)

    def get_total_orders_count(self) -> int:
        """Получить общее количество выполненных заказов"""
        return int(self.driver.find_element(*self.locators.TOTAL_ORDERS_COUNT).text)

    def get_today_orders_count(self) -> int:
        """Получить количество заказов за сегодня"""
        return int(self.driver.find_element(*self.locators.TODAY_ORDERS_COUNT).text)

    def get_orders_in_progress_numbers(self) -> list[int]:
        """Получить номера заказов в работе"""
        elements = self.driver.find_elements(*self.locators.ORDERS_IN_PROGRESS)
        return [int(element.text) for element in elements]

