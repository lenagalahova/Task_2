import allure
from config import ErrorMessege


class TestLoginUser:
    @allure.title("Логин нового пользователя")
    @allure.description("Создание и логин пользователя")
    def test_login_new_user(self, stocks_api, register_new_user):
        body = register_new_user

        response = stocks_api.login_user(json=body)
        assert response.status_code == 200
        assert response.json()["success"]

    @allure.title("Логин несуществующей почтой")
    def test_login_non_existent_email(
        self, stocks_api, register_new_user
    ):
        invalid_body = {
        "email": "wrong_" + register_new_user["email"],
        "password": register_new_user["password"]
    }

        response = stocks_api.login_user(json=invalid_body)
        assert response.status_code == 401
        assert ErrorMessege.NOTENOUGHT_DATA_FOR_LOGIN in response.json()["message"]

    @allure.title("Логин несуществующим паролем")
    def test_login_non_existent_password(
        self, stocks_api, register_new_user
    ):
        invalid_body = {
        "email": register_new_user["email"],
        "password": "wrong_" + register_new_user["password"]
    }

        response = stocks_api.login_user(json=invalid_body)
        assert response.status_code == 401
        assert ErrorMessege.NOTENOUGHT_DATA_FOR_LOGIN in response.json()["message"]
