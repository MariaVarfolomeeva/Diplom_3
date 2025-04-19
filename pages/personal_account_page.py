from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountLocators


class PersonalAccountPage(BasePage):
    PATH = "/account/profile"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = PersonalAccountLocators()

    def is_profile_page_opened(self) -> bool:
        """Проверка, что открыта страница профиля"""
        return self.is_element_present(self.locators.PROFILE_FORM)

    def go_to_order_history(self) -> None:
        """Перейти в раздел истории заказов"""
        self.click_element(self.locators.ORDER_HISTORY_LINK)

    def is_order_history_active(self) -> bool:
        """Проверка активности раздела истории заказов"""
        return "active" in self.driver.find_element(
            *self.locators.ORDER_HISTORY_LINK
        ).get_attribute("class")

    def logout(self) -> None:
        """Выйти из аккаунта"""
        self.click_element(self.locators.LOGOUT_BUTTON)

    def get_order_history_items_count(self) -> int:
        """Получить количество заказов в истории"""
        return len(self.driver.find_elements(*self.locators.ORDER_HISTORY_ITEM))

