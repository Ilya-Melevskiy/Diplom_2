import requests
import allure

from urls.urls import GET_ORDERS_USER


class TestGetOrdersUser:

    @allure.title(
        "Получение заказов конкретного пользователя -"
        "для авторизованного пользователя возвращает 200"
    )
    def test_get_orders_user_auth_user_return_200(
        self, login_user, add_ingredient_for_user
    ):
        response = requests.get(
            GET_ORDERS_USER,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )
        assert response.status_code == 200


    @allure.title(
        "Получение заказов конкретного пользователя -"
        "для авторизованного пользователя возвращает true в success"
    )
    def test_get_orders_user_auth_user_return_success_true(
        self, login_user, add_ingredient_for_user
    ):
        response = requests.get(
            GET_ORDERS_USER,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )
        assert response.json()["success"] is True


    @allure.title(
        "Получение заказов конкретного пользователя -"
        "для авторизованного пользователя возвращает orders с корректными данными"
    )
    def test_get_orders_user_auth_user_return_correct_orders(
        self, login_user, add_ingredient_for_user
    ):
        response = requests.get(
            GET_ORDERS_USER,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )
        assert (
            len(response.json()["orders"]) == 1
            and response.json()["orders"][0]["ingredients"]
            == add_ingredient_for_user["ingredients"]
        )


    @allure.title(
        "Получение заказов конкретного пользователя -"
        "для авторизованного пользователя возвращает не пустой total"
    )
    def test_get_orders_user_auth_user_return_not_empty_total(
        self, login_user, add_ingredient_for_user
    ):
        response = requests.get(
            GET_ORDERS_USER,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )
        assert response.json()["total"]


    @allure.title(
        "Получение заказов конкретного пользователя -"
        "для авторизованного пользователя возвращает не пустой total_today"
    )
    def test_get_orders_user_auth_user_return_not_empty_total_today(
        self, login_user, add_ingredient_for_user
    ):
        response = requests.get(
            GET_ORDERS_USER,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )
        assert response.json()["totalToday"]


    @allure.title(
        "Получение заказов конкретного пользователя -"
        "для неавторизованного пользователя возвращает 401"
    )
    def test_get_orders_user_unauth_user_return_401(self):
        response = requests.get(GET_ORDERS_USER)
        assert response.status_code == 401


    @allure.title(
        "Получение заказов конкретного пользователя -"
        "для неавторизованного пользователя возвращает false в success"
    )
    def test_get_orders_user_unauth_user_return_success_false(self):
        response = requests.get(GET_ORDERS_USER)
        assert response.json()["success"] is False


    @allure.title(
        "Получение заказов конкретного пользователя -"
        "для неавторизованного пользователя возвращает корректное сообщение"
    )
    def test_get_orders_user_unauth_user_return_correct_message(self):
        response = requests.get(GET_ORDERS_USER)
        assert response.json()["message"] == "You should be authorised"
