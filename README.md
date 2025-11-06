# Diplom_2
# Автотесты для Api Stellar Burgers
### Реализованные сценарии

Созданы api-тесты для:

`Создание пользователя`,
`Изменение пользователя`,
`Авторизация пользователя`,
`Создание заказа`,
`Получение заказов конкретного пользователя`

### Структура проекта
- `data` - данные для тестов:
    `data.py`
- `helpers` - вспомогательные функции:
    `helpers.py`
- `urls` - эндпоинты:
    `urls.py`
- `tests` - api-автотесты:
    `test_change_user.py`, 
    `test_create_order.py`,
    `test_create_user.py`,
    `test_get_orders_user.py`,
    `test_login_user.py`

### Запуск автотестов

`$ pytest -v`

**Установка зависимостей**

> `$ pip install -r requirements.txt`
