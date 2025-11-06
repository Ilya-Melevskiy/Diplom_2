import pytest
import requests

from helpers.helpers import Helpers
from data import data
from urls.urls import CREATE_USER, DEL_USER, LOGIN_USER, CREATE_ORDER


@pytest.fixture
def create_del_user():
    email = f'{Helpers.generate_random_string(10)}@mail.ru'
    password = Helpers.generate_random_string(10)
    name = Helpers.generate_random_string(10)

    payload = {'email': email,
                'password': password,
                'name': name}
    
    response = requests.post(CREATE_USER, json=payload)

    if response.status_code == 200:
        login_pass = payload


    yield {'login_pass': login_pass, 'response': response}

    access_token = response.json()['accessToken']
    requests.delete(DEL_USER, json=payload, headers={'Authorization': access_token})


@pytest.fixture
def login_user(create_del_user):
    email = create_del_user['login_pass']['email']
    password = create_del_user['login_pass']['password']
    name = create_del_user['login_pass']['name']
    login_pass = {'email': email,
                'password': password,
                'name' : name
                }
    payload = {'email': email,
                'password': password
                }
    
    response = requests.post(LOGIN_USER, json=payload)

    return {'response': response, 'login_pass': login_pass}


@pytest.fixture
def add_ingredient_for_user(login_user):
    ingredients = [data.ingredients[0]['id']]
    payload = {'ingredients': ingredients}
    
    response = requests.post(CREATE_ORDER, json=payload, headers={'Authorization': login_user['response'].json()['accessToken']})

    return {'response': response, 'ingredients' : ingredients}