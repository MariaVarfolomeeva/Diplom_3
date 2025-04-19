from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    """Локаторы личного кабинета"""
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ACTIVE_TAB = (By.XPATH, "//a[contains(@class, 'active')]")
    PROFILE_FORM = (By.XPATH, "//form[contains(@class, 'Profile_form')]")
    ORDER_HISTORY_ITEM = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem')]")

