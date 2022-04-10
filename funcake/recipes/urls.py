from django.urls import path

from funcake.recipes.views import (
    RecipeListView,
    RecipeDetailView,
)

app_name = "recipes"
urlpatterns = [
    path("", view=RecipeListView.as_view(), name="list"),
    path("<str:pk>/", view=RecipeDetailView.as_view(), name="detail"),
]
