import pytest
import requests
import allure

from urls.urls import LOGIN_USER
from data import data


class TestLoginUser:

    @allure.title("Авторизация пользователя -с корректными данными возвращает 200")
    def test_login_user_correct_existing_data_return_200_status_code(self, login_user):
        assert login_user["response"].status_code == 200


    @allure.title(
        "Авторизация пользователя -с корректными данными возвращает true в success"
    )
    def test_login_user_correct_existing_data_return_success_true(self, login_user):
        assert login_user["response"].json()["success"] is True


    @allure.title(
        "Авторизация пользователя -"
        "с корректными данными возвращает не пустой accessToken"
    )
    def test_login_user_correct_existing_data_return_not_empty_access_token(
        self, login_user
    ):
        assert "Bearer" in login_user["response"].json()["accessToken"]


    @allure.title(
        "Авторизация пользователя -с корректными данными возвращает refreshToken"
    )
    def test_login_user_correct_existing_data_return_refresh_token(self, login_user):
        assert login_user["response"].json()["refreshToken"]


    @allure.title(
        "Авторизация пользователя -с корректными данными возвращает корректный email"
    )
    def test_login_user_correct_existing_data_return_user_email(self, login_user):
        assert (
            login_user["login_pass"]["email"]
            == login_user["response"].json()["user"]["email"]
        )


    @allure.title(
        "Авторизация пользователя -с корректными данными возвращает корректный name"
    )
    def test_login_user_correct_existing_data_return_user_name(self, login_user):
        assert (
            login_user["login_pass"]["name"]
            == login_user["response"].json()["user"]["name"]
        )


    @pytest.mark.parametrize(
        "email, password",
        [
            (data.user_data_new_email, "exist_password"),
            ("exist_email", data.user_data_new_password),
            ("", "exist_password"),
            ("exist_email", ""),
        ],
        ids=["incorrect_email", "incorrect_password", "empty_email", "empty_password"],
    )
    def test_login_user_incorrect_data_return_401_status_code(
        self, create_del_user, email, password, request
    ):
        allure.dynamic.title(
            f"Авторизация пользователя - c {request.node.callspec.id}возвращает 401"
        )
        email_payload = (
            create_del_user["login_pass"]["email"]
            if email == "exist_email"
            else email
            if email
            else ""
        )
        password_payload = (
            create_del_user["login_pass"]["password"]
            if password == "exist_email"
            else password
            if password
            else ""
        )

        payload = {"email": email_payload, "password": password_payload}
        response = requests.post(LOGIN_USER, json=payload)

        assert response.status_code == 401


    @pytest.mark.parametrize(
        "email, password",
        [
            (data.user_data_new_email, "exist_password"),
            ("exist_email", data.user_data_new_password),
            ("", "exist_password"),
            ("exist_email", ""),
        ],
        ids=["incorrect_email", "incorrect_password", "empty_email", "empty_password"],
    )
    def test_login_user_incorrect_data_return_success_false(
        self, create_del_user, email, password, request
    ):
        allure.dynamic.title(
            f"Авторизация пользователя - c {request.node.callspec.id}"
            f"возвращает false в success"
        )
        email_payload = (
            create_del_user["login_pass"]["email"]
            if email == "exist_email"
            else email
            if email
            else ""
        )
        password_payload = (
            create_del_user["login_pass"]["password"]
            if password == "exist_email"
            else password
            if password
            else ""
        )

        payload = {"email": email_payload, "password": password_payload}
        response = requests.post(LOGIN_USER, json=payload)

        assert response.json()["success"] is False


    @pytest.mark.parametrize(
        "email, password",
        [
            (data.user_data_new_email, "exist_password"),
            ("exist_email", data.user_data_new_password),
            ("", "exist_password"),
            ("exist_email", ""),
        ],
        ids=["incorrect_email", "incorrect_password", "empty_email", "empty_password"],
    )
    def test_login_user_incorrect_data_return_correct_message(
        self, create_del_user, email, password, request
    ):
        allure.dynamic.title(
            f"Авторизация пользователя - c {request.node.callspec.id}"
            f"возвращает корректное сообщение"
        )
        email_payload = (
            create_del_user["login_pass"]["email"]
            if email == "exist_email"
            else email
            if email
            else ""
        )
        password_payload = (
            create_del_user["login_pass"]["password"]
            if password == "exist_email"
            else password
            if password
            else ""
        )

        payload = {"email": email_payload, "password": password_payload}
        response = requests.post(LOGIN_USER, json=payload)

        assert response.json()["message"] == "email or password are incorrect"
