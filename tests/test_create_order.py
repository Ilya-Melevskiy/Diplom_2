import requests
import pytest
import allure

from data import data
from urls.urls import CREATE_ORDER


class TestCreateOrder:

    @pytest.mark.parametrize(
        "id",
        [
            data.ingredients[0]["id"],
            data.ingredients[1]["id"],
            data.ingredients[2]["id"],
        ],
        ids=[
            data.ingredients[0]["name"],
            data.ingredients[1]["name"],
            data.ingredients[2]["name"],
        ],
    )
    def test_create_order_auth_user_with_ingredients_return_200(self, login_user, id, request):
        allure.dynamic.title(f'Создание заказа - для авторизованного пользователя '
                             f'с ингредиентом {request.node.callspec.id} возвращает 200')
        payload = {"ingredients": [id]}
        response = requests.post(
            CREATE_ORDER,
            json=payload,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )

        assert response.status_code == 200


    @pytest.mark.parametrize(
        "id",
        [
            data.ingredients[0]["id"],
            data.ingredients[1]["id"],
            data.ingredients[2]["id"],
        ],
        ids=[
            data.ingredients[0]["name"],
            data.ingredients[1]["name"],
            data.ingredients[2]["name"],
        ],
    )
    def test_create_order_auth_user_with_ingredients_return_success_true(
        self, login_user, id, request
    ):
        allure.dynamic.title(f'Создание заказа - для авторизованного пользователя '
                             f'с ингредиентом {request.node.callspec.id} '
                             f'возвращает true в success')
        payload = {"ingredients": [id]}
        response = requests.post(
            CREATE_ORDER,
            json=payload,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )

        assert response.json()["success"] is True


    @pytest.mark.parametrize(
        "index",
        [0, 1, 2],
        ids=[
            data.ingredients[0]["name"],
            data.ingredients[1]["name"],
            data.ingredients[2]["name"],
        ],
    )
    def test_create_order_auth_user_with_ingredients_return_correct_name_burger(
        self, login_user, index, request
    ):
        allure.dynamic.title(f'Создание заказа - для авторизованного пользователя '
                             f'с ингредиентом {request.node.callspec.id} '
                             f'возвращает корректное имя: {data.ingredients[index]["name_burger"]}')
        payload = {"ingredients": [data.ingredients[index]["id"]]}
        response = requests.post(
            CREATE_ORDER,
            json=payload,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )

        assert response.json()["name"] == data.ingredients[index]["name_burger"]


    @pytest.mark.parametrize(
        "id",
        [
            data.ingredients[0]["id"],
            data.ingredients[1]["id"],
            data.ingredients[2]["id"],
        ],
        ids=[
            data.ingredients[0]["name"],
            data.ingredients[1]["name"],
            data.ingredients[2]["name"],
        ],
    )
    def test_create_order_auth_user_with_ingredients_return_not_empty_order_number(
        self, login_user, id, request
    ):
        allure.dynamic.title(f'Создание заказа - для авторизованного пользователя '
                             f'с ингредиентом {request.node.callspec.id} '
                             f'возвращает не пустой order_number')
        payload = {"ingredients": [id]}
        response = requests.post(
            CREATE_ORDER,
            json=payload,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )

        assert response.json()["order"]["number"]


    @pytest.mark.parametrize(
        "id",
        [
            data.ingredients[0]["id"],
            data.ingredients[1]["id"],
            data.ingredients[2]["id"],
        ],
        ids=[
            data.ingredients[0]["name"],
            data.ingredients[1]["name"],
            data.ingredients[2]["name"],
        ],
    )
    def test_create_order_unauth_user_with_ingredients_return_200(self, id, request):
        allure.dynamic.title(f'Создание заказа - для неавторизованного пользователя '
                             f'с ингредиентом {request.node.callspec.id} '
                             f'возвращает 200')
        payload = {"ingredients": [id]}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.status_code == 200


    @pytest.mark.parametrize(
        "id",
        [
            data.ingredients[0]["id"],
            data.ingredients[1]["id"],
            data.ingredients[2]["id"],
        ],
        ids=[
            data.ingredients[0]["name"],
            data.ingredients[1]["name"],
            data.ingredients[2]["name"],
        ],
    )
    def test_create_order_unauth_user_with_ingredients_return_success_true(self, id, request):
        allure.dynamic.title(f'Создание заказа - для неавторизованного пользователя '
                             f'с ингредиентом {request.node.callspec.id} '
                             f'возвращает true в success')
        payload = {"ingredients": [id]}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.json()["success"] is True


    @pytest.mark.parametrize(
        "index",
        [0, 1, 2],
        ids=[
            data.ingredients[0]["name"],
            data.ingredients[1]["name"],
            data.ingredients[2]["name"],
        ],
    )
    def test_create_order_unauth_user_with_ingredients_return_correct_name_burger(
        self, index, request
    ):
        allure.dynamic.title(f'Создание заказа - для неавторизованного пользователя '
                             f'с ингредиентом {request.node.callspec.id} возвращает '
                             f'корректное имя: {data.ingredients[index]["name_burger"]}')
        payload = {"ingredients": [data.ingredients[index]["id"]]}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.json()["name"] == data.ingredients[index]["name_burger"]


    @pytest.mark.parametrize(
        "id",
        [
            data.ingredients[0]["id"],
            data.ingredients[1]["id"],
            data.ingredients[2]["id"],
        ],
        ids=[
            data.ingredients[0]["name"],
            data.ingredients[1]["name"],
            data.ingredients[2]["name"],
        ],
    )
    def test_create_order_unauth_user_with_ingredients_return_not_empty_order_number(
        self, id, request
    ):
        allure.dynamic.title(f'Создание заказа - для неавторизованного пользователя '
                             f'с ингредиентом {request.node.callspec.id} возвращает '
                             f'не пустой order_number')
        payload = {"ingredients": [id]}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.json()["order"]["number"]


    @allure.title('Создание заказа - для неавторизованного пользователя ' \
                    'без ингредиентов возвращает 400')
    def test_create_order_unauth_user_without_ingredients_return_400(self):
        payload = {"ingredients": []}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.status_code == 400


    @allure.title('Создание заказа - для неавторизованного пользователя ' \
                    'без ингредиентов возвращает false в success')
    def test_create_order_unauth_user_without_ingredients_return_success_false(self):
        payload = {"ingredients": []}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.json()["success"] is False


    @allure.title('Создание заказа - для неавторизованного пользователя ' \
                    'без ингредиентов возвращает корректное сообщение')
    def test_create_order_unauth_user_without_ingredients_return_message(self):
        payload = {"ingredients": []}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.json()["message"] == "Ingredient ids must be provided"


    @allure.title('Создание заказа - для неавторизованного пользователя ' \
                    'с ингредиентом с некорректным id возвращает 500')
    def test_create_order_unauth_user_with_ingredient_incorrect_id_return_500(self):
        payload = {"ingredients": ["123"]}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.status_code == 500
