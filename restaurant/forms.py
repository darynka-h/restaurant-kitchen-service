from __future__ import annotations
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from restaurant.models import Dish, Cook


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "To find dish type enter a name "
                               "and press 'Enter'"
            }
        )

    )


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "To find dish enter a name and press 'Enter' "
            }
        )

    )


class CookCreationForm(UserCreationForm):
    # photo = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
            "photo",
        )

    def clean_years_of_experience(self):
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]

    def clean_years_of_experience(self):
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


def validate_years_of_experience(
    years_of_experience: float | str,
) -> int:       # check if years_of_experience is integer
    if not isinstance(years_of_experience, int):
        raise ValidationError("Experience should be integer")
    elif years_of_experience < 1:
        raise ValidationError("Experience should be more or equal than 1 year")

    return years_of_experience


class CookSearchForm(forms.Form):
    first_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "To find cook enter first name and press "
                               "'Enter'"
            }
        )
    )
