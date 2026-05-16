import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def create_new_user_and_return_login_password():

    local_part = generate_random_string(10)
    email = f"{local_part}@ya.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)

    return {"email": email, "password": password, "name": name}

