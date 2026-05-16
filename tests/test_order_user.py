import allure
from config import ErrorMessege, ingredients


class TestGetOrderUser:
    @allure.title("Получение заказа авторизированным пользователем")
    def test_get_order_auth_user(self, stocks_api, register_new_user):
        order_data = {"ingredients": ingredients}
        response_order = stocks_api.create_order(
            access_token=register_new_user["accessToken"], json=order_data
        )
        assert "number" in response_order.json()["order"]
        response = stocks_api.get_order_user(
            access_token=register_new_user["accessToken"]
        )
        assert response.status_code == 200
        assert response.json()["success"]
        assert "orders" in response.json()

    @allure.title("Получение заказа неавторизированным пользователем")
    def test_get_order_notauth_user(self, stocks_api):
        order_data = {"ingredients": ingredients}
        response_order = stocks_api.create_order(access_token=None, json=order_data)
        assert "number" in response_order.json()["order"]

        response = stocks_api.get_order_user(access_token=None)
        assert response.status_code == 401
        assert not response.json()["success"]
        assert response.json()["message"] == ErrorMessege.WITHOUT_AUTH
