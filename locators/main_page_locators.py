from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/constructor']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href='/orders']")
