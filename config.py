BASE_URL = "https://qa-stellarburgers.education-services.ru/"

USER_CREATE_ENDPOINT = "/api/auth/register"
USER_LOGIN_ENDPOINT = "/api/auth/login"
UPDATE_USER_DATA = "/api/auth/user"
CREATE_ORDERS_ENDPOINT = "/api/orders"
ORDERS_USER_ENDPOINT = "/api/orders"

ingredients = ["691577430cc94f001a65b859", "691577430cc94f001a65b85f"]
invalid_ingredients = ["77430cc", "a65b85f"]


class ErrorMessege:
    LOGIN_ALREADY_USED = "User already exists"
    INSUFFICIENT_DATA = "Email, password and name are required fields"
    NOTENOUGHT_DATA_FOR_LOGIN = "email or password are incorrect"
    WITHOUT_AUTH = "You should be authorised"
    WITHOUT_ING = "Ingredient ids must be provided"
