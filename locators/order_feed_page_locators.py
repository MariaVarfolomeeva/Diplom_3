from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    ORDER_ITEM = (By.XPATH, "//div[@class='order-item']")
    ORDER_DETAILS_BUTTON = (By.XPATH, "//button[@class='order-details-btn']")
    ORDER_LIST = (By.XPATH, "//div[@class='orders-list']")
