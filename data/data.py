from helpers.helpers import Helpers


user_data_without_email = ('', Helpers.generate_random_string(10), Helpers.generate_random_string(10))
user_data_without_password= (f'{Helpers.generate_random_string(10)}@mail.ru', '', Helpers.generate_random_string(10))
user_data_without_name= (f'{Helpers.generate_random_string(10)}@mail.ru', Helpers.generate_random_string(10), '')

user_data_new_email = f'{Helpers.generate_random_string(10)}@mail.ru'
user_data_new_password = Helpers.generate_random_string(10)
user_data_new_name = Helpers.generate_random_string(10)

ingredients = [{'id': '61c0c5a71d1f82001bdaaa6d', 'name': 'Fluorescent bun R2-D3', 'name_burger': 'Флюоресцентный бургер'},
               {'id': '61c0c5a71d1f82001bdaaa6f', 'name': 'The meat of the immortal mollusks Protostomia', 'name_burger': 'Бессмертный бургер'},
               {'id': '61c0c5a71d1f82001bdaaa70', 'name': 'Beef meteorite (chop)', 'name_burger': 'Метеоритный бургер'}]
