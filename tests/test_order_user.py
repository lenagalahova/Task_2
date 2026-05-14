import allure
from config import ErrorMessege, ingredients


class TestGetOrderUser:
    @allure.title("Получение заказа авторизированным пользователем")
    def test_get_order_auth_user(self, stocks_api, registered_user):
        order_data = {"ingredients": ingredients}
        response_order = stocks_api.create_order(
            access_token=registered_user["accessToken"], json=order_data
        )
        assert "number" in response_order.json()["order"]
        response = stocks_api.get_order_user(
            access_token=registered_user["accessToken"]
        )
        assert response.json()["success"]
        assert "orders" in response.json()

    @allure.title("Получение заказа неавторизированным пользователем")
    def test_get_order_notauth_user(self, stocks_api):
        order_data = {"ingredients": ingredients}
        response_order = stocks_api.create_order(access_token=None, json=order_data)
        assert "number" in response_order.json()["order"]

        response = stocks_api.get_order_user(access_token=None)
        assert not response.json()["success"]
        assert response.json()["message"] == ErrorMessege.WITHOUT_AUTH
