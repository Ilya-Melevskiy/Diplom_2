import requests
import pytest
import allure

from data import data
from urls.urls import CREATE_ORDER


class TestCreateOrder:

    @pytest.mark.parametrize(
        "index",
        [0, 1, 2],
        ids=[
            data.ingredients[0]["name"],
            data.ingredients[1]["name"],
            data.ingredients[2]["name"],
        ],
    )
    def test_success_create_order_with_ingredients_for_auth_user(
        self, login_user, index, request
    ):
        allure.dynamic.title(f'Создание заказа - успешное создание заказа для авторизованного пользователя '
                             f'с ингредиентом {request.node.callspec.id}')
        payload = {"ingredients": [data.ingredients[index]["id"]]}
        response = requests.post(
            CREATE_ORDER,
            json=payload,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["name"] == data.ingredients[index]["name_burger"]
        assert response.json()["order"]["number"]


    @pytest.mark.parametrize(
        "index",
        [0, 1, 2],
        ids=[
            data.ingredients[0]["name"],
            data.ingredients[1]["name"],
            data.ingredients[2]["name"],
        ],
    )
    def test_success_create_order_with_ingredients_for_unauth_user(
        self, index, request
    ):
        allure.dynamic.title(f'Создание заказа - успешное создание заказа для неавторизованного пользователя '
                             f'с ингредиентом {request.node.callspec.id}')
        payload = {"ingredients": [data.ingredients[index]["id"]]}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["name"] == data.ingredients[index]["name_burger"]
        assert response.json()["order"]["number"]


    @allure.title('Создание заказа - для неавторизованного пользователя ' \
                    'без ингредиентов возвращает 400')
    def test_create_order_without_ingredients_for_unauth_user_return_400(self):
        payload = {"ingredients": []}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == "Ingredient ids must be provided"


    @allure.title('Создание заказа - для неавторизованного пользователя ' \
                    'с ингредиентом с некорректным id возвращает 500')
    def test_create_order_with_ingredient_incorrect_id_for_unauth_user__return_500(self):
        payload = {"ingredients": ["123"]}
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.status_code == 500
