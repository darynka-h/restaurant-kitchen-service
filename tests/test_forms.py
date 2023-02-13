# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
# from restaurant.models import Cook
#
#
# class FormTest(TestCase):
#     def test_cook_creation_form_with_experience_first_last_name_photo(self):
#         new_cook = Cook(
#             username="cook_111",
#             # password1="cook123test",
#             # password2="cook123test",
#             years_of_experience=7,
#             first_name="CookTest",
#             last_name="CookSur",
#                        )
#         new_cook.photo = SimpleUploadedFile(
#             name='cook.png',
#             content=open("staticfiles/uploads/photos/cook.png", 'rb').read(),
#             content_type='image/jpeg'
#         )
#
#         new_cook.save()
#         self.assertEqual(Cook.objects.count(), 1)
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from restaurant.forms import CookCreationForm
from restaurant.models import Cook


class FormTest(TestCase):
    def test_cook_creation_form_with_experience_first_last_name_photo(self):
        form_data = {
            "username": "new_cook",
            "password1": "user123test",
            "password2": "user123test",
            "years_of_experience": 12,
            "first_name": "Cook",
            "last_name": "Shift",
        }
        file_data = {
            "photo": SimpleUploadedFile(
                name="cook_image.png",
                content=open("tests/cook_image.png", "rb").read(),
                content_type="image/png"
            )
        }
        form = CookCreationForm(form_data, file_data)
        print(form.errors)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(Cook.objects.count(), 1)
