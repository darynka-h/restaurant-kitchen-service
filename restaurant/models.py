from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)
    dish_type_image = models.ImageField(upload_to="photos/", null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="photos/", null=True, blank=True)

    class Meta:
        ordering = ["username"]
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    dish_image = models.ImageField(upload_to="photos/", null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
