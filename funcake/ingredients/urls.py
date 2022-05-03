from django.urls import path

from funcake.ingredients.views import (
    IngredientListView,
    IngredientUpdateView,
    IngredientCreateView,
    IngredientDeleteView,
)

app_name = "ingredients"
urlpatterns = [
    path("", view=IngredientListView.as_view(), name="list"),
    path("create/", view=IngredientCreateView.as_view(), name="create"),
    path("<int:pk>/", view=IngredientUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", view=IngredientDeleteView.as_view(), name="delete"),
]
