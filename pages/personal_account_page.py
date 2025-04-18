from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PersonalAccountPage:
    URL = "https://stellarburgers.nomoreparties.site/account/profile"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def is_loaded(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/account/profile') and contains(@class, 'active')]"))
        )

    def go_to_order_history(self):
        history_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/account/orders')]"))
        )
        history_tab.click()

    def is_order_history_section_active(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/account/orders') and contains(@class, 'active')]"))
        )

    def logout(self):
        logout_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))
        )
        logout_button.click()
