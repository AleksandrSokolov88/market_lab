import allure
import pytest
import requests
from utils.base_url import BASE_URL as BASE_URL
from utils.header import HEADER as HEADER
from utils.create_test_data import create_data
from utils.admin_assert import admin_assert


class TestRegisterUser:

    @pytest.mark.parametrize("data", create_data("test/register_user/data/data_correct_email.yaml"))
    def test_email_positive(self, data):
        allure.dynamic.title(f"Тест: {data[0]}")
        with allure.step("Отправить POST запрос на /auth/register с тест датой в body"):
            response = requests.post(BASE_URL + "auth/register", headers=HEADER, json=data[1])
        with allure.step("Проверяем статус код"):
            assert response.status_code == 200
        with allure.step("Проверяем что пришел ответ"):
            assert response.json() is not None
        with allure.step("Проверяем что пользователь есть в списке пользователей"):
            try:
                is_created = False
                name, domen = data[1]["email"].split("@")
                email = f"{name}@{domen.lower()}"
                for user in admin_assert():
                    if email == user["email"]:
                        is_created = True
                assert is_created
            except AssertionError as e:
                with allure.step(f"Ожидали {data[1]["email"]} получили {user["email"]}"):
                    raise e
