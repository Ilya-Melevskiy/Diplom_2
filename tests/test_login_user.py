import pytest
import requests
import allure

from urls.urls import LOGIN_USER
from data import data


class TestLoginUser:

    @allure.title("Авторизация пользователя - успешная авторизация с корректными данными")
    def test_login_user_correct_existing_data_return_200_status_code(self, login_user):
        assert login_user["response"].status_code == 200
        assert login_user["response"].json()["success"] is True
        assert "Bearer" in login_user["response"].json()["accessToken"]
        assert login_user["response"].json()["refreshToken"]
        assert (
            login_user["login_pass"]["email"]
            == login_user["response"].json()["user"]["email"]
        )
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
            f"Авторизация пользователя - c {request.node.callspec.id} возвращает 401"
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
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"


        
