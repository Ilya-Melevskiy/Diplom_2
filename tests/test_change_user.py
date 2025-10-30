import requests
import pytest
import allure

from data import data
from urls.urls import CHANGE_USER, LOGIN_USER


class TestChangeUser:
    @pytest.mark.parametrize(
        'field, new_value',
        [
            ('email', data.user_data_new_email),
            ('name', data.user_data_new_name),
            ('password', data.user_data_new_password),
        ],
        ids=['email', 'name', 'password'],
    )
    def test_change_user_auth_user_change_field_return_200(
        self, login_user, field, new_value, request
    ):
        allure.dynamic.title(
            f'Изменение пользователя - для авторизованного пользователя '
            f'изменение поля {request.node.callspec.id} возвращает 200'
        )
        payload = {field: new_value}
        response = requests.patch(
            CHANGE_USER,
            json=payload,
            headers={'Authorization': login_user['response'].json()['accessToken']},
        )

        assert response.status_code == 200


    @pytest.mark.parametrize(
        'field, new_value',
        [
            ('email', data.user_data_new_email),
            ('name', data.user_data_new_name),
            ('password', data.user_data_new_password),
        ],
        ids=['email', 'name', 'password'],
    )
    def test_change_user_auth_user_change_field_return_success_true(
        self, login_user, field, new_value, request
    ):
        allure.dynamic.title(
            f'Изменение пользователя - для авторизованного пользователя '
            f'изменение поля {request.node.callspec.id} возвращает true в success'
        )
        payload = {field: new_value}
        response = requests.patch(
            CHANGE_USER,
            json=payload,
            headers={'Authorization': login_user['response'].json()['accessToken']},
        )

        assert response.json()['success'] is True


    @pytest.mark.parametrize(
        'field, new_value',
        [
            ('email', data.user_data_new_email),
            ('name', data.user_data_new_name),
            ('password', data.user_data_new_password),
        ],
        ids=['email', 'name', 'password'],
    )
    def test_change_user_auth_user_change_field_return_correct_user_email(
        self, login_user, field, new_value, request
    ):
        allure.dynamic.title(
            f'Изменение пользователя - для авторизованного пользователя '
            f'изменение поля {request.node.callspec.id} возвращает корректное сообщение'
        )
        payload = {field: new_value}
        response = requests.patch(
            CHANGE_USER,
            json=payload,
            headers={'Authorization': login_user['response'].json()['accessToken']},
        )
        correct_email = (
            new_value if field == 'email' else login_user['login_pass']['email']
        )

        assert response.json()['user']['email'] == correct_email


    @pytest.mark.parametrize(
        'field, new_value',
        [
            ('email', data.user_data_new_email),
            ('name', data.user_data_new_name),
            ('password', data.user_data_new_password),
        ],
        ids=['email', 'name', 'password'],
    )
    def test_change_user_auth_user_change_field_return_correct_user_name(
        self, login_user, field, new_value, request
    ):
        allure.dynamic.title(
            f'Изменение пользователя - для авторизованного пользователя '
            f'изменение поля {request.node.callspec.id} возвращает user_name'
        )
        payload = {field: new_value}
        response = requests.patch(
            CHANGE_USER,
            json=payload,
            headers={'Authorization': login_user['response'].json()['accessToken']},
        )
        correct_name = (
            new_value if field == 'name' else login_user['login_pass']['name']
        )

        assert response.json()['user']['name'] == correct_name


    @pytest.mark.parametrize(
        'field, new_value',
        [
            ('email', data.user_data_new_email),
            ('name', data.user_data_new_name),
            ('password', data.user_data_new_password),
        ],
        ids=['email', 'name', 'password'],
    )
    def test_change_user_auth_user_change_field_login_with_new_data_return_200(
        self, login_user, field, new_value, request
    ):
        allure.dynamic.title(
            f'Изменение пользователя - после изменения поля '
            f'{request.node.callspec.id} можно успешно авторизоваться'
        )
        payload = {field: new_value}
        requests.patch(
            CHANGE_USER,
            json=payload,
            headers={'Authorization': login_user['response'].json()['accessToken']},
        )

        email = new_value if field == 'email' else login_user['login_pass']['email']
        password = (
            new_value if field == 'password' else login_user['login_pass']['password']
        )
        payload_login = {'email': email, 'password': password}
        response = requests.post(LOGIN_USER, json=payload_login)

        assert response.status_code == 200


    @pytest.mark.parametrize(
        'field, new_value',
        [
            ('email', data.user_data_new_email),
            ('name', data.user_data_new_name),
            ('password', data.user_data_new_password),
        ],
        ids=['email', 'name', 'password'],
    )
    def test_change_user_unauth_user_change_field_return_401(
        self, field, new_value, request
    ):
        allure.dynamic.title(
            f'Изменение пользователя - для неавторизованного пользователя '
            f'изменение поля {request.node.callspec.id} возвращает 401'
        )
        payload = {field: new_value}
        response = requests.patch(CHANGE_USER, json=payload)

        assert response.status_code == 401


    @pytest.mark.parametrize(
        'field, new_value',
        [
            ('email', data.user_data_new_email),
            ('name', data.user_data_new_name),
            ('password', data.user_data_new_password),
        ],
        ids=['email', 'name', 'password'],
    )
    def test_change_user_unauth_user_change_field_return_success_false(
        self, field, new_value, request
    ):
        allure.dynamic.title(
            f'Изменение пользователя - для неавторизованного пользователя '
            f'изменение поля {request.node.callspec.id} возвращает false в success'
        )
        payload = {field: new_value}
        response = requests.patch(CHANGE_USER, json=payload)

        assert response.json()['success'] is False


    @pytest.mark.parametrize(
        'field, new_value',
        [
            ('email', data.user_data_new_email),
            ('name', data.user_data_new_name),
            ('password', data.user_data_new_password),
        ],
        ids=['email', 'name', 'password'],
    )
    def test_change_user_unauth_user_change_field_return_correct_message(
        self, field, new_value, request
    ):
        allure.dynamic.title(
            f'Изменение пользователя - для неавторизованного пользователя '
            f'изменение поля {request.node.callspec.id} возвращает корректное сообщение'
        )
        payload = {field: new_value}
        response = requests.patch(CHANGE_USER, json=payload)

        assert response.json()['message'] == 'You should be authorised'
