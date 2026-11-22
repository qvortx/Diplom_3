import random
import string
import requests
import allure
from faker import Faker
from data import Urls

fake = Faker()


def generate_random_string(length=6):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


@allure.step("Сгенерировать данные тестового пользователя")
def generate_user_payload():
    return {
        "email": f"{fake.user_name()}_{generate_random_string()}@yandex.ru",
        "password": fake.password(length=10, special_chars=False),
        "name": fake.first_name()
    }


class UserApi:

    @staticmethod
    @allure.step("Создать тестового пользователя через API")
    def create_user(payload):
        return requests.post(Urls.API_REGISTER_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Удалить тестового пользователя через API")
    def delete_user(access_token):
        return requests.delete(
            Urls.API_USER_ENDPOINT,
            headers={"Authorization": access_token}
        )
