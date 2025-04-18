import requests


class ApiClient:
    BASE_URL = "https://your-api-url.com/api"

    def create_order_via_api(self, access_token, ingredients=None):
        url = f"{self.BASE_URL}/orders"
        headers = {"Authorization": f"Bearer {access_token}"}
        default_ingredients = ["ingredient1", "ingredient2"]
        data = {"ingredients": ingredients or default_ingredients}

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get("orderNumber")

    def get_total_done_count(self):
        url = f"{self.BASE_URL}/orders/total"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("total")
