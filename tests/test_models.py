from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import DishType, Dish


class ModelTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test")

        self.assertEqual(
            str(dish_type), f"{dish_type.name}"
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="cook",
            password="cook12345",
            first_name="Cook first",
            last_name="Cook last",
        )

        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="test")
        dish = Dish.objects.create(
            name="Dish_1",
            dish_type=dish_type
        )

        self.assertEqual(str(dish), f"{dish.name}")

    def test_cook_with_experience(self):
        username = "cook"
        password = "cook12345"
        years_of_experience = 13
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
