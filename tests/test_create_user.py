import allure
from config import ErrorMessege
from helpers.create_random_user import create_new_user_and_return_login_password


class TestUser:
    @allure.title("Создание нового пользователя")
    @allure.description("Создание пользователя")
    def test_create_new_user(
        self, stocks_api):
        body = create_new_user_and_return_login_password()
        response = stocks_api.create_new_user(json=body)
        assert response.status_code == 200
        assert response.json()["success"]
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_new_same_user(
        self, stocks_api):
        body = create_new_user_and_return_login_password()
        response_1 = stocks_api.create_new_user(json=body)
        assert response_1.json()["success"]

        response_2 = stocks_api.create_new_user(json=body)
        assert response_2.status_code == 403
        assert ErrorMessege.LOGIN_ALREADY_USED in response_2.json()["message"]

    @allure.title("Создание пользователя без почты")
    def test_create_new_user_without_email(
        self, stocks_api, new_user_data_without_email
    ):
        body = new_user_data_without_email
        response = stocks_api.create_new_user(json=body)

        assert response.status_code == 403
        assert ErrorMessege.INSUFFICIENT_DATA in response.json()["message"]

    @allure.title("Создание пользователя без пароля")
    def test_create_new_user_without_password(
        self, stocks_api, new_user_data_without_password
    ):
        body = new_user_data_without_password
        response = stocks_api.create_new_user(json=body)

        assert response.status_code == 403
        assert ErrorMessege.INSUFFICIENT_DATA in response.json()["message"]

    @allure.title("Создание пользователя без пароля")
    def test_create_new_user_without_name(self, stocks_api, new_user_data_without_name):
        body = new_user_data_without_name
        response = stocks_api.create_new_user(json=body)

        assert response.status_code == 403
        assert ErrorMessege.INSUFFICIENT_DATA in response.json()["message"]
