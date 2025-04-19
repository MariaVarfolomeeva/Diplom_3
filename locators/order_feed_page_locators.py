from selenium.webdriver.common.by import By


class OrderFeedLocators:
    """Локаторы для ленты заказов"""
    ORDER_ITEM = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem')]")
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'OrderDetails')]")
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close')]")

