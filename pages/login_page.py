from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from config.urls import Urls
from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    PATH = Urls.LOGIN

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.HEADER)

    def enter_email(self, email: str) -> None:
        self.send_keys(self.locators.EMAIL_INPUT, email)

    def enter_password(self, password: str) -> None:
        self.send_keys(self.locators.PASSWORD_INPUT, password)

    def click_submit(self) -> None:
        self.click_element(self.locators.SUBMIT_BUTTON)

    def login(self, email: str, password: str) -> None:
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit()
        self.wait.until(EC.url_changes(f"{Urls.LOGIN}"))

    def click_forgot_password_link(self) -> None:
        self.click_element(self.locators.FORGOT_PASSWORD_LINK)
        self.wait.until(EC.url_contains("forgot-password"))

    def click_register_link(self) -> None:
        self.click_element(self.locators.REGISTER_LINK)
        self.wait.until(EC.url_contains("register"))

    def get_error_message(self) -> str:
        return self.wait.until(
            EC.visibility_of_element_located(self.locators.ERROR_MESSAGE)
        ).text

    def is_error_visible(self) -> bool:
        return self.is_element_present(self.locators.ERROR_MESSAGE)

    def is_redirect_to_register(self) -> bool:
        return Urls.REGISTER in self.driver.current_url

