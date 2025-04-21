from dataclasses import dataclass


class TestData:
    """
    Основной класс тестовых данных.
    Сохраняет оригинальные названия переменных для совместимости с существующими тестами.
    """
    USER_EMAIL = "test_user@example.com"
    USER_PASSWORD = "test_password"
    INVALID_EMAIL = "invalid_user@example.com"
    INVALID_PASSWORD = "wrong_password"
    RECOVERY_EMAIL = "recovery@example.com"

    INGREDIENTS = {
        "bun": "Булка с кунжутом",
        "cheese": "Сыр чеддер",
        "lettuce": "Листья салата"
    }

    ORDER_DETAILS = {
        "bun": 2,
        "cheese": 1,
        "lettuce": 1
    }


@dataclass
class TestUser:
    """
    Класс тестового пользователя.
    Сохраняет оригинальные названия полей.
    """
    email: str = "test@example.com"
    password: str = "correct_password"


class TestIngredients:
    BUN = TestData.INGREDIENTS["bun"]
    CHEESE = TestData.INGREDIENTS["cheese"]
    LETTUCE = TestData.INGREDIENTS["lettuce"]


