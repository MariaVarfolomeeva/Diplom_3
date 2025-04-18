import pytest
import logging
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from utils.test_data import recovery_email
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)



@pytest.mark.usefixtures("driver_setup")
class TestPasswordRecovery:

    def test_can_open_password_recovery_page(self, driver):
        logger.info("Тест: переход на страницу восстановления пароля")
        login = LoginPage(driver)
        login.click_forgot_password_link()

        current_url = driver.current_url
        assert "reset-password" in current_url, f"Не перешли на страницу восстановления. URL: {current_url}"

    def test_submit_recovery_email(self, driver):
        logger.info("Тест: ввод почты и клик по кнопке 'Восстановить'")
        recovery = PasswordRecoveryPage(driver)
        recovery.enter_email(recovery_email)
        recovery.click_recover_button()

        url_after = driver.current_url
        assert "reset-password" not in url_after, "Похоже, остались на той же странице — возможно, запрос не отправился"

    def test_password_field_becomes_active_when_eye_icon_clicked(self, driver):
        logger.info("Тест: проверка активации поля при нажатии на иконку 'глаз'")

        recovery = PasswordRecoveryPage(driver)

        try:
            recovery.click_eye_icon()
            password_field = driver.find_element(By.NAME, "password")
            class_list = password_field.get_attribute("class")

            is_highlighted = "input_status_active" in class_list
            assert is_highlighted, "Поле пароля не стало активным после клика на 'глаз'"
        except NoSuchElementException:
            pytest.fail("Не удалось найти поле пароля или иконку 'глаз'")
