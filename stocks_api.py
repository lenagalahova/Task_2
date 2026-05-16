import requests
from allure import step
from config import (
    BASE_URL,
    USER_CREATE_ENDPOINT,
    USER_LOGIN_ENDPOINT,
    UPDATE_USER_DATA,
    CREATE_ORDERS_ENDPOINT,
    ORDERS_USER_ENDPOINT,
)


class StockApi:
    @step("Создание пользователя")
    def create_new_user(self, **kwargs):
        return requests.post(f"{BASE_URL}{USER_CREATE_ENDPOINT}", **kwargs)

    @step("Логин пользователя в системе")
    def login_user(self, **kwargs):
        return requests.post(f"{BASE_URL}{USER_LOGIN_ENDPOINT}", **kwargs)

    @step("Изменение данных пользователя в системе")
    def update_user_data(self, access_token=None, **kwargs):
        headers = {"Authorization": access_token}
        return requests.patch(
            f"{BASE_URL}{UPDATE_USER_DATA}", headers=headers, **kwargs
        )

    @step("Создание заказа")
    def create_order(self, access_token=None, **kwargs):
        headers = {"Authorization": access_token}
        return requests.post(
            f"{BASE_URL}{CREATE_ORDERS_ENDPOINT}", headers=headers, **kwargs
        )

    @step("Получение списка заказов")
    def get_order_user(self, access_token=None, **kwargs):
        headers = {"Authorization": access_token}
        return requests.get(
            f"{BASE_URL}{ORDERS_USER_ENDPOINT}", headers=headers, **kwargs
        )
