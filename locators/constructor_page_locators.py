from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    """Класс локаторов для страницы конструктора бургеров"""

    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")

    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_COUNTER = (By.XPATH, "//span[contains(@class, 'Counter_counter')]")

    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_title')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_close')]")

    @staticmethod
    def get_ingredient_by_type(ingredient_type: str):
        """Получить локатор для конкретного типа ингредиента"""
        return (By.XPATH,
                f"//div[contains(@class, 'ingredient') and contains(., '{ingredient_type}')]")
