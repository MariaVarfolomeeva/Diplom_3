import pytest
import logging
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.test_data import TestData

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("driver_setup")
class TestLoginFlow:

    def test_go_to_login_page_from_main(self, driver):
        logger.info("Открываем главную страницу и переходим на страницу логина")
        main = MainPage(driver)
        main.click_login_link()

        assert "login" in driver.current_url, "Не перешли на страницу входа"

    def test_login_with_valid_credentials(self, driver):
        logger.info("Проверяем логин с валидными данными")
        login_screen = LoginPage(driver)

        login_screen.perform_login(TestData.USER_EMAIL, TestData.USER_PASSWORD)

        try:
            driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
            success = True
        except:
            success = False

        assert success, "Пользователь не авторизован — кнопка оформления заказа не найдена"

    def test_login_with_wrong_password(self, driver):
        logger.info("Проверяем логин с неверным паролем")
        login_screen = LoginPage(driver)

        login_screen.perform_login(TestData.USER_EMAIL, "12345_не_тот_пароль")

        try:
            error_msg = driver.find_element(By.CLASS_NAME, "input__error").text
        except:
            error_msg = ""

        assert "неверный" in error_msg.lower(), "Ожидалось сообщение об ошибке логина"

