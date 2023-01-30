from django.urls import path

from .views import index, DishTypeListView, DishListView, CookListView, CookDetailView, DishDetailView

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail",
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cooks-list",
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
]

app_name = "restaurant"
