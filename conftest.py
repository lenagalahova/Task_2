import pytest
from stocks_api import StockApi
from helpers.create_random_user import (
    create_new_user_and_return_login_password,
    register_new_user,
)


@pytest.fixture
def new_user_data():
    return create_new_user_and_return_login_password()


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
def registered_user():
    return register_new_user()


@pytest.fixture
def registered_user_with_invalid_email():
    full_data = register_new_user()
    payload = {"email": "invalid_email", "password": full_data["password"]}
    return payload


@pytest.fixture
def registered_user_with_invalid_passwird():
    full_data = register_new_user()
    payload = {"email": full_data["email"], "password": "invalid_passwird"}
    return payload


@pytest.fixture
def stocks_api():
    return StockApi()
