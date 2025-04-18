from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    URL = "https://stellarburgers.nomoreparties.site/"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def is_loaded(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Собери бургер']"))
        )

    def click_personal_account(self):
        personal_account_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/account/profile']"))
        )
        personal_account_button.click()
