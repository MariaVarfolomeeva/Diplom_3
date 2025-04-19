from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    PATH = "/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.ORDER_BUTTON)

    def click_login_link(self) -> None:
        self.click_element(self.locators.LOGIN_LINK)

    def click_profile_link(self) -> None:
        self.click_element(self.locators.PROFILE_LINK)

    def click_constructor_link(self) -> None:
        self.click_element(self.locators.CONSTRUCTOR_LINK)

    def click_feed_link(self) -> None:
        self.click_element(self.locators.FEED_LINK)

    def add_ingredient_to_constructor(self, ingredient_type: str) -> None:
        ingredient = self.driver.find_element(*self.locators.INGREDIENT_ITEM)
        constructor_area = self.driver.find_element(*self.locators.CONSTRUCTOR_AREA)
        ActionChains(self.driver).drag_and_drop(ingredient, constructor_area).perform()

    def click_order_button(self) -> None:
        self.click_element(self.locators.ORDER_BUTTON)

    def is_order_modal_visible(self) -> bool:
        return self.is_element_present(self.locators.MODAL)

    def close_order_modal(self) -> None:
        self.click_element(self.locators.MODAL_CLOSE)

    def get_order_number(self) -> str:
        return self.driver.find_element(*self.locators.ORDER_NUMBER).text

    def get_current_url(self) -> str:
        """Возвращает текущий URL (инкапсуляция driver.current_url)"""
        return self.driver.current_url


