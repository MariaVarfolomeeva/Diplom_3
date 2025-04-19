from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators


class ConstructorPage(BasePage):
    """Page Object для страницы конструктора бургеров"""

    PATH = "/constructor"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = ConstructorPageLocators()

    def is_opened(self) -> bool:
        """Проверка загрузки страницы конструктора"""
        return self.is_element_present(self.locators.ORDER_BUTTON)

    def add_ingredient(self, ingredient_type: str) -> None:
        """
        Добавить ингредиент в конструктор
        :param ingredient_type: Тип ингредиента (bun/sauce/main)
        """
        locator = self.locators.get_ingredient_by_type(ingredient_type)
        ingredient = self.wait.until(EC.element_to_be_clickable(locator))
        target = self.driver.find_element(*self.locators.CONSTRUCTOR_AREA)
        ActionChains(self.driver).drag_and_drop(ingredient, target).perform()

    def get_ingredient_count(self) -> int:
        """Получить количество добавленных ингредиентов"""
        counter = self.driver.find_element(*self.locators.ORDER_COUNTER)
        return int(counter.text) if counter.text else 0

    def make_order(self) -> str:
        """
        Оформить заказ
        :return: Номер заказа
        """
        self.click_element(self.locators.ORDER_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.locators.ORDER_MODAL))
        return self.driver.find_element(*self.locators.ORDER_NUMBER).text

    def close_order_modal(self) -> None:
        """Закрыть модальное окно заказа"""
        self.click_element(self.locators.MODAL_CLOSE)
        self.wait.until(EC.invisibility_of_element_located(self.locators.ORDER_MODAL))

