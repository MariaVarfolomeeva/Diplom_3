from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from config.urls import Urls
from .base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators


class ConstructorPage(BasePage):
    PATH = Urls.CONSTRUCTOR

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = ConstructorPageLocators()

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.ORDER_BUTTON)

    def add_ingredient(self, ingredient_type: str) -> None:
        locator = self.locators.get_ingredient_by_type(ingredient_type)
        ingredient = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Ингредиент типа {ingredient_type} не найден или не кликабелен"
        )
        target = self.driver.find_element(*self.locators.CONSTRUCTOR_AREA)
        ActionChains(self.driver).drag_and_drop(ingredient, target).perform()

    def get_ingredient_count(self) -> int:
        try:
            counter = self.driver.find_element(*self.locators.ORDER_COUNTER)
            return int(counter.text) if counter.text else 0
        except:
            return 0

    def make_order(self) -> str:
        self.click_element(self.locators.ORDER_BUTTON)
        self.wait.until(
            EC.visibility_of_element_located(self.locators.ORDER_MODAL),
            message="Модальное окно заказа не появилось"
        )
        return self.driver.find_element(*self.locators.ORDER_NUMBER).text

    def close_order_modal(self) -> None:
        self.click_element(self.locators.MODAL_CLOSE)
        self.wait.until(
            EC.invisibility_of_element_located(self.locators.ORDER_MODAL),
            message="Модальное окно заказа не закрылось"
        )

