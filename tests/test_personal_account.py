import pytest
import logging
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from utils.test_data import TestUser

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("driver_setup")
class TestPersonalAccount:

    def test_go_to_personal_account(self, driver, test_user: TestUser):
        logger.info("Авторизуемся и переходим в личный кабинет")

        login = LoginPage(driver)
        login.open()
        login.login(test_user.email, test_user.password)

        main = MainPage(driver)
        main.open()
        main.click_personal_account()

        account_page = PersonalAccountPage(driver)
        assert account_page.is_loaded(), "Не удалось попасть в личный кабинет"

    def test_go_to_order_history(self, driver, test_user: TestUser):
        logger.info("Переход в раздел 'История заказов' из личного кабинета")

        login = LoginPage(driver)
        login.open()
        login.login(test_user.email, test_user.password)

        account_page = PersonalAccountPage(driver)
        account_page.open()
        account_page.go_to_order_history()

        assert account_page.is_order_history_section_active(), "Раздел 'История заказов' не активен"

    def test_logout(self, driver, test_user: TestUser):
        logger.info("Выходим из аккаунта через личный кабинет")

        login = LoginPage(driver)
        login.open()
        login.login(test_user.email, test_user.password)

        account_page = PersonalAccountPage(driver)
        account_page.open()
        account_page.logout()

        login_page = LoginPage(driver)
        assert login_page.is_loaded(), "После выхода из аккаунта не попали на страницу логина"
