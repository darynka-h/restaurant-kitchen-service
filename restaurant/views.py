from django.shortcuts import render
from django.views import generic

from restaurant.models import Cook, Dish, DishType


def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }
    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "restaurant/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishListView(generic.ListView):
    queryset = Dish.objects.all().select_related("dish_type")
    model = Dish
    template_name = "restaurant/dish_list.html"
    context_object_name = "dish_list"


class DishDetailView(generic.DetailView):
    model = Dish
    field = "__all__"
    template_name = "restaurant/dish_detail.html"


class CookListView(generic.ListView):
    model = Cook
    template_name = "restaurant/cook_list.html"
    context_object_name = "cook_list"


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")
    template_name = "restaurant/cook_detail.html"
