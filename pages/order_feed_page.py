from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class OrderFeedPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    ORDER_ITEM = (By.XPATH, "//div[@class='order-item']")
    ORDER_DETAILS_BUTTON = (By.XPATH, "//button[@class='order-details-btn']")
    ORDER_LIST = (By.XPATH, "//div[@class='orders-list']")

    def open(self):
        self.driver.get("https://example.com/orders")

    def click_on_order(self, order_index):
        orders = self.driver.find_elements(*self.ORDER_ITEM)
        orders[order_index].click()

    def get_order_details(self):
        return self.driver.find_element(*self.ORDER_DETAILS_BUTTON).text

    def get_all_orders(self):
        return [order.text for order in self.driver.find_elements(*self.ORDER_ITEM)]
