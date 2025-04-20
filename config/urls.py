class Urls:
    BASE = "https://stellarburgers.nomoreparties.site"

    HOME = BASE
    CONSTRUCTOR = f"{BASE}/constructor"
    LOGIN = f"{BASE}/login"
    REGISTER = f"{BASE}/register"
    FORGOT_PASSWORD = f"{BASE}/forgot-password"
    RESET_PASSWORD = f"{BASE}/reset-password"
    ACCOUNT_PROFILE = f"{BASE}/account/profile"
    ORDER_HISTORY = f"{BASE}/account/orders"
    FEED = f"{BASE}/feed"

    API_LOGIN = f"{BASE}/api/auth/login"
    API_LOGOUT = f"{BASE}/api/auth/logout"
    API_REGISTER = f"{BASE}/api/auth/register"
    API_USER = f"{BASE}/api/auth/user"
    API_ORDERS = f"{BASE}/api/orders"

    @staticmethod
    def ingredient_detail(ingredient_id: str) -> str:
        """Генерация URL для детальной страницы ингредиента"""
        return f"{Urls.BASE}/ingredients/{ingredient_id}"

    @staticmethod
    def order_detail(order_number: str) -> str:
        """Генерация URL для детальной страницы заказа"""
        return f"{Urls.FEED}/{order_number}"