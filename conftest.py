import pytest
from stocks_api import StockApi
from helpers.create_random_user import create_new_user_and_return_login_password


@pytest.fixture
def new_user_data_without_email():
    full_data = create_new_user_and_return_login_password()
    payload = {"password": full_data["password"], "name": full_data["name"]}
    return payload


@pytest.fixture
def new_user_data_without_password():
    full_data = create_new_user_and_return_login_password()
    payload = {"email": full_data["email"], "name": full_data["name"]}
    return payload


@pytest.fixture
def new_user_data_without_name():
    full_data = create_new_user_and_return_login_password()
    payload = {"email": full_data["email"], "password": full_data["password"]}
    return payload


@pytest.fixture
def register_new_user(stocks_api):
    user_data = create_new_user_and_return_login_password()
    response = stocks_api.create_new_user(json=user_data)

    assert response.status_code == 200, f"Ошибка: {response.json()}"

    response_json = response.json()

    return {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "accessToken": response_json.get("accessToken"),
        "refreshToken": response_json.get("refreshToken"),
    }


@pytest.fixture
def stocks_api():
    return StockApi()
