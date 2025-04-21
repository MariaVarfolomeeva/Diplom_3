import pytest
from utils.driver_factory import DriverFactory
from utils.test_data import TestData
from pages.login_page import LoginPage
from utils.test_data import TestUser


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("browser")
    driver = DriverFactory.create_driver(browser)

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def test_user():
    return TestData.USER_EMAIL, TestData.USER_PASSWORD


@pytest.fixture
def login(driver):
    """Фикстура для авторизации перед тестами"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(TestUser.email, TestUser.password)
    yield


@pytest.fixture
def authorized_user(driver):
    """Фикстура для предварительной авторизации пользователя"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(TestUser.email, TestUser.password)
    yield driver
