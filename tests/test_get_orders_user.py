import requests
import allure

from urls.urls import GET_ORDERS_USER


class TestGetOrdersUser:

    @allure.title(
        "Получение заказов конкретного пользователя -"
        "успешное получение заказов для авторизованного пользователя "
    )
    def test_get_orders_user_auth_user_return_200(
        self, login_user, add_ingredient_for_user
    ):
        response = requests.get(
            GET_ORDERS_USER,
            headers={"Authorization": login_user["response"].json()["accessToken"]},
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert (
            len(response.json()["orders"]) == 1
            and response.json()["orders"][0]["ingredients"]
            == add_ingredient_for_user["ingredients"]
        )
        assert response.json()["total"]
        assert response.json()["totalToday"]


    @allure.title(
        "Получение заказов конкретного пользователя -"
        "для неавторизованного пользователя возвращает 401"
    )
    def test_get_orders_user_unauth_user_return_401(self):
        response = requests.get(GET_ORDERS_USER)

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "You should be authorised"
        
