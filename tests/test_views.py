from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from restaurant.models import DishType, Cook, Dish

DISH_TYPE_URL = reverse("restaurant:dish-type-list")
COOK_URL = reverse("restaurant:cook-list")
DISH_URL = reverse("restaurant:dish-list")


class PublicDishTYpeTest(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_TYPE_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "Test", "123password123"
        )
        self.client.force_login(self.user)
        DishType.objects.create(name="Pizza")
        DishType.objects.create(name="Pasta")
        DishType.objects.create(name="Biscuit")
        DishType.objects.create(name="Bistro")
    def test_dish_type_retrieve(self):
        response = self.client.get(DISH_TYPE_URL)
        dish_types = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]), list(dish_types)
        )
        self.assertTemplateUsed(response, "restaurant/dish_type_list.html")

    def test_dish_type_search_form_with_name(self):
        response = self.client.get(DISH_TYPE_URL, {
            "name": "bis"
        })
        dish_types = DishType.objects.all()
        queryset = dish_types.filter(name__icontains="bis")
        self.assertEqual(list(
            response.context["dish_type_list"]), list(queryset)
        )

    def test_dish_type_search_form_with_name_which_doesnt_exist(self):
        response = self.client.get(DISH_TYPE_URL, {
            "name": "abab"
        })
        dish_types = DishType.objects.all()
        queryset = dish_types.filter(name__icontains="abab")
        self.assertEqual(
            list(response.context["dish_type_list"]), list(queryset)
        )

    def test_manufacturer_search_form_with_simular_names(self):
        response = self.client.get(DISH_TYPE_URL, {
            "name": "Bis"
        })
        dish_types = DishType.objects.all()
        queryset = dish_types.filter(name__icontains="Bis")
        self.assertEqual(
            list(response.context["dish_type_list"]), list(queryset)
        )


class PrivateCookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "Test", "123password123"
        )
        self.client.force_login(self.user)
        Cook.objects.create(username="user_1", first_name="Cook_busy", years_of_experience=7)
        Cook.objects.create(username="user_2", first_name="Test_cook", years_of_experience=16)
        Cook.objects.create(username="user_3", first_name="Best_cook", years_of_experience=5)

    def test_create_cook(self):
        form_data = {
            "username": "new_cook_1",
            "password1": "user123test1",
            "password2": "user123test1",
            "years_of_experience": 5,
            "first_name": "Cook",
            "last_name": "Boss",
            "photo": SimpleUploadedFile(
                    name="cook_image_2.png",
                    content=open("tests/cook_image_2.png", "rb").read(),
                    content_type="image/png"
                )
        }

        # file_data = {
        #     "photo": SimpleUploadedFile(
        #         name="cook_image_2.png",
        #         content=open("tests/cook_image_2.png", "rb").read(),
        #         content_type="image/png"
        #     )
        # }

        self.client.post(reverse("restaurant:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])
        new_user.save()
        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])

    def test_cook_search_form_with_first_name(self):
        response = self.client.get(COOK_URL, {
            "first_name": "busy"
        })
        cooks = Cook.objects.all()
        queryset = cooks.filter(first_name__icontains="busy")
        self.assertEqual(list(response.context["cook_list"]), list(queryset))

    def test_cook_search_form_with_username_which_doesnt_exist(self):
        response = self.client.get(COOK_URL, {
            "first_name": "kUHAR"
        })
        cooks = Cook.objects.all()
        queryset = cooks.filter(first_name__icontains="kUHAR")
        self.assertEqual(list(response.context["cook_list"]), list(queryset))

    def test_cook_search_form_with_simular_usernames(self):
        response = self.client.get(COOK_URL, {
            "first_name": "cook"
        })
        cooks = Cook.objects.all()
        queryset = cooks.filter(first_name__icontains="cook")
        self.assertEqual(list(response.context["cook_list"]), list(queryset))


class PrivateDishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "Test", "123password123"
        )
        self.client.force_login(self.user)
        dish_type = DishType.objects.create(name="Pasta")
        Dish.objects.create(name="Karbonara", dish_type=dish_type)
        Dish.objects.create(name="Bolonietti", dish_type=dish_type)
        Dish.objects.create(name="Spaghetti", dish_type=dish_type)

    def test_dish_search_form_with_name(self):
        response = self.client.get(DISH_URL, {"name": "ra"})
        dishes = Dish.objects.all()
        queryset = dishes.filter(name__icontains="ra")
        self.assertEqual(list(response.context["dish_list"]), list(queryset))

    def test_dish_search_form_with_name_which_doesnt_exist(self):
        response = self.client.get(DISH_URL, {"name": "carrot"})
        dishes = Dish.objects.all()
        queryset = dishes.filter(name__icontains="carrot")
        self.assertEqual(list(response.context["dish_list"]), list(queryset))

    def test_dish_search_form_with_simular_names(self):
        response = self.client.get(DISH_URL, {
            "name": "etti"
        })
        dishes = Dish.objects.all()
        queryset = dishes.filter(name__icontains="etti")
        self.assertEqual(list(response.context["dish_list"]), list(queryset))
