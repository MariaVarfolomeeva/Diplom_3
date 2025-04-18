import pytest
from utils.driver_factory import DriverFactory
from utils.test_data import TestData


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
