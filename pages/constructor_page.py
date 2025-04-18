from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ConstructorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    INGREDIENT_ITEM = (By.XPATH, "//div[@class='ingredient-item']")
    ADD_TO_ORDER_BUTTON = (By.XPATH, "//button[@class='add-to-order']")
    ORDER_COUNTER = (By.XPATH, "//span[@class='order-counter']")
    ORDER_SUMMARY_BUTTON = (By.XPATH, "//button[@class='order-summary']")

    def open(self):
        self.driver.get("https://example.com/constructor")

    def click_on_ingredient(self, index):
        ingredients = self.driver.find_elements(*self.INGREDIENT_ITEM)
        ingredients[index].click()

    def add_ingredient_to_order(self):
        self.driver.find_element(*self.ADD_TO_ORDER_BUTTON).click()

    def get_order_counter(self):
        return self.driver.find_element(*self.ORDER_COUNTER).text

    def go_to_order_summary(self):
        self.driver.find_element(*self.ORDER_SUMMARY_BUTTON).click()
