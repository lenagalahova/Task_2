import allure
from config import ErrorMessege


class TestLoginUser:
    @allure.title("Логин нового пользователя")
    @allure.description("Создание и логин пользователя")
    def test_login_new_user(self, stocks_api, registered_user):
        body = registered_user

        response = stocks_api.login_user(json=body)
        assert response.json()["success"]

    @allure.title("Логин несуществующей почтой")
    def test_login_non_existent_email(
        self, stocks_api, registered_user_with_invalid_email
    ):
        body = registered_user_with_invalid_email

        response = stocks_api.login_user(json=body)
        assert response.status_code == 401
        assert ErrorMessege.NOTENOUGHT_DATA_FOR_LOGIN in response.json()["message"]

    @allure.title("Логин несуществующим паролем")
    def test_login_non_existent_password(
        self, stocks_api, registered_user_with_invalid_passwird
    ):
        body = registered_user_with_invalid_passwird

        response = stocks_api.login_user(json=body)
        assert response.status_code == 401
        assert ErrorMessege.NOTENOUGHT_DATA_FOR_LOGIN in response.json()["message"]
