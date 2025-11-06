import requests
import pytest
import allure

from urls.urls import CREATE_USER
from data import data


class TestCreateUser:
    @allure.title('Создание пользователя - успешное создание пользователя при вводе корректных данных')
    def test_create_user_correct_data_return_200_status_code(self, create_del_user):
        assert create_del_user['response'].status_code == 200
        assert create_del_user['response'].json()['success'] is True
        assert (
            create_del_user['response'].json()['user']['email']
            == create_del_user['login_pass']['email']
        )
        assert (
            create_del_user['response'].json()['user']['name']
            == create_del_user['login_pass']['name']
        )
        assert 'Bearer' in create_del_user['response'].json()['accessToken']
        assert create_del_user['response'].json()['refreshToken']
        

    @allure.title(
        'Создание пользователя - создание пользователя c данными уже существующего пользователя возвращает 403'
    )
    def test_create_user_existing_user_data_return_403_status_code(
        self, create_del_user
    ):
        email = create_del_user['login_pass']['email']
        password = create_del_user['login_pass']['password']
        name = create_del_user['login_pass']['name']
        payload = {'email': email, 'password': password, 'name': name}
        response = requests.post(CREATE_USER, json=payload)

        assert response.status_code == 403
        assert response.json()['success'] is False
        assert response.json()['message'] == 'User already exists'
        

    @pytest.mark.parametrize(
        'email, password, name',
        [
            data.user_data_without_email,
            data.user_data_without_password,
            data.user_data_without_name,
        ],
        ids=['email', 'password', 'name'],
    )
    def test_create_user_without_required_field_return_403_status_code(
        self, email, password, name, request
    ):
        allure.dynamic.title(
            f'Создание пользователя - без обязательного поля '
            f'{request.node.callspec.id} возвращает 403'
        )
        payload = {'email': email, 'password': password, 'name': name}

        response = requests.post(CREATE_USER, json=payload)

        assert response.status_code == 403
        assert response.json()['success'] is False
        assert (
            response.json()['message'] == 'Email, password and name are required fields'
        )


