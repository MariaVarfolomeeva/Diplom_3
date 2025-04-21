from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    LOGIN_LINK = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']")
    FEED_LINK = (By.XPATH, "//a[@href='/feed']")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_close')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_title')]")

