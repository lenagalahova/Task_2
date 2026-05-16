import allure
from config import ErrorMessege, ingredients, invalid_ingredients


class TestCreateOrder:
    @allure.title("Создание заказа с авторизированным пользователем")
    def test_create_order(self, stocks_api, register_new_user):
        order_data = {"ingredients": ingredients}
        response_order = stocks_api.create_order(
            access_token=register_new_user["accessToken"], json=order_data
        )

        assert response_order.status_code == 200
        assert "order" in response_order.json()
        assert "number" in response_order.json()["order"]
        assert response_order.json()["success"]

    @allure.title(
        "Создание заказа с авторизированным пользователем и невалидным ингредиентом"
    )
    def test_create_order_invalid_ingredients(self, stocks_api, register_new_user):
        order_data = {"ingredients": invalid_ingredients}
        response_order = stocks_api.create_order(
            access_token=register_new_user["accessToken"], json=order_data
        )

        assert response_order.status_code == 500

    @allure.title("Создание заказа с авторизированным пользователем без ингредиентов")
    def test_create_order_without_ingredients(self, stocks_api, register_new_user):
        order_data = {}
        response_order = stocks_api.create_order(
            access_token=register_new_user["accessToken"], json=order_data
        )

        assert response_order.status_code == 400
        assert response_order.json()["message"] == ErrorMessege.WITHOUT_ING

    @allure.title("Создание заказа неавторизированным пользователем")
    def test_create_order_without_auth(self, stocks_api):
        order_data = {"ingredients": ingredients}
        response_order = stocks_api.create_order(access_token=None, json=order_data)

        assert response_order.status_code == 200
        assert "order" in response_order.json()
        assert "number" in response_order.json()["order"]
        assert response_order.json()["success"]

    @allure.title("Создание заказа неавторизированным пользователем и без ингредиентов")
    def test_create_order_without_auth_withuot_ingredients(self, stocks_api):
        order_data = {}
        response_order = stocks_api.create_order(access_token=None, json=order_data)

        assert response_order.status_code == 400
        assert response_order.json()["message"] == ErrorMessege.WITHOUT_ING

    @allure.title(
        "Создание заказа неавторизированным пользователем и невалидным ингредиентами"
    )
    def test_create_order_without_auth_invalid_ingredients(self, stocks_api):
        order_data = {"ingredients": invalid_ingredients}
        response_order = stocks_api.create_order(access_token=None, json=order_data)

        assert response_order.status_code == 500
