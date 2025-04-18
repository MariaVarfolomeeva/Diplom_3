import pytest
import logging
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from utils.test_data import TestUser, TestData
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("driver_setup")
class TestMainFunctionality:
    @pytest.fixture
    def test_user(self):
        """Фикстура для тестового пользователя"""
        return TestUser(
            email=TestData.USER_EMAIL,
            password=TestData.USER_PASSWORD,
            name="Test User"
        )

    def test_go_to_constructor(self, driver):
        logger.info("Проверка перехода на страницу конструктора по клику")

        main = MainPage(driver)
        main.open()
        main.click_constructor_link()

        assert "constructor" in driver.current_url or ConstructorPage(driver).is_loaded(), "Не перешли в конструктор"

    def test_go_to_order_feed(self, driver):
        logger.info("Проверка перехода в ленту заказов")

        main = MainPage(driver)
        main.open()
        main.click_order_feed_link()

        assert "feed" in driver.current_url, "Не перешли в ленту заказов"

    def test_ingredient_modal_opens_and_closes(self, driver):
        logger.info("Проверка модального окна с ингредиентом")

        constructor = ConstructorPage(driver)
        constructor.open()

        ingredient = constructor.get_any_ingredient()
        ingredient_name = ingredient.text
        ingredient.click()

        assert constructor.is_ingredient_modal_open(), "Модалка с ингредиентом не открылась"

        constructor.close_ingredient_modal()
        assert not constructor.is_ingredient_modal_open(), "Модалка не закрылась"

    def test_ingredient_counter_increases(self, driver):
        logger.info("Проверка увеличения счётчика ингредиента при добавлении в заказ")

        constructor = ConstructorPage(driver)
        constructor.open()

        bun = constructor.get_bun()
        constructor.drag_bun_to_cart(bun)

        ing = constructor.get_any_ingredient()
        initial = constructor.get_ingredient_counter(ing)
        constructor.drag_ingredient_to_cart(ing)

        updated = constructor.get_ingredient_counter(ing)
        assert updated == initial + 1, f"Счётчик не увеличился: было {initial}, стало {updated}"

    def test_logged_user_can_place_order(self, driver, test_user: TestUser):
        logger.info("Проверка, что залогиненный пользователь может оформить заказ")

        login = LoginPage(driver)
        login.open()
        login.login(test_user.email, test_user.password)

        constructor = ConstructorPage(driver)
        constructor.open()

        constructor.drag_bun_to_cart(constructor.get_bun())
        constructor.drag_ingredient_to_cart(constructor.get_any_ingredient())

        constructor.click_order_button()

        try:
            is_order_confirmed = constructor.wait_for_order_confirmation()
            assert is_order_confirmed, "Заказ не был оформлен"
        except NoSuchElementException:
            pytest.fail("Не появилось подтверждение заказа")
