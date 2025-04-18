from dataclasses import dataclass


class TestData:
    USER_EMAIL = "test_user@example.com"
    USER_PASSWORD = "test_password"
    INVALID_EMAIL = "invalid_user@example.com"
    INVALID_PASSWORD = "wrong_password"

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


recovery_email = "recovery@example.com"


@dataclass
class TestUser:
    email: str
    password: str
    name: str = "Test User"
    access_token: str = None
