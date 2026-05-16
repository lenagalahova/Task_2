import allure
from config import ErrorMessege
from helpers.create_random_user import generate_random_string



class TestUpdateUser:
    @allure.title("Обновление почты зарегистрированного пользователя")
    def test_update_email_with_auth(self, stocks_api, register_new_user):
        new_email = f"{generate_random_string(10)}@ya.ru"
        update_data = {"email": new_email}
        response = stocks_api.update_user_data(
            register_new_user["accessToken"], json=update_data
        )
        assert response.status_code == 200
        assert response.json()["success"]
        assert response.json()["user"]["email"] == new_email

    @allure.title("Обновление пароля зарегистрированного пользователя")
    def test_update_password_with_auth(self, stocks_api, register_new_user):
        new_password = f"{generate_random_string(10)}"
        update_data = {"password": new_password}
        response = stocks_api.update_user_data(
            register_new_user["accessToken"], json=update_data
        )
        assert response.status_code == 200
        assert response.json()["success"]

    @allure.title("Обновление имени зарегистрированного пользователя")
    def test_name_password_with_auth(self, stocks_api, register_new_user):
        new_name = f"{generate_random_string(10)}"
        update_data = {"name": new_name}
        response = stocks_api.update_user_data(
            register_new_user["accessToken"], json=update_data
        )
        assert response.status_code == 200
        assert response.json()["success"]
        assert response.json()["user"]["name"] == new_name

    @allure.title("Обновление почты незарегистрированного пользователя")
    def test_update_email_without_auth(self, stocks_api):
        new_email = f"{generate_random_string(10)}@ya.ru"
        update_data = {"email": new_email}
        response = stocks_api.update_user_data(json=update_data)
        assert response.status_code == 401
        assert response.json()["message"] == ErrorMessege.WITHOUT_AUTH

    @allure.title("Обновление имени без авторизации")
    def test_update_name_without_auth(self, stocks_api):
        new_name = f"{generate_random_string(10)}"
        update_data = {"name": new_name}
        response = stocks_api.update_user_data(json=update_data)
        assert response.status_code == 401
        assert response.json()["message"] == ErrorMessege.WITHOUT_AUTH

    @allure.title("Обновление пароля без авторизации")
    def test_update_password_without_auth(self, stocks_api):
        new_password = f"{generate_random_string(10)}"
        update_data = {"password": new_password}
        response = stocks_api.update_user_data(json=update_data)
        assert response.status_code == 401
        assert response.json()["message"] == ErrorMessege.WITHOUT_AUTH
