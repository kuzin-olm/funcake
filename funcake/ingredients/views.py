from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, ListView, UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy

from .models import Ingredient
from .forms import IngredientForm


class IngredientListView(LoginRequiredMixin, ListView):
    template_name = "ingredients/list.html"
    model = Ingredient
    context_object_name = "ingredients"

    def get_queryset(self):
        return self.model.objects.order_by("name")


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "ingredients/update.html"
    model = Ingredient
    form_class = IngredientForm
    context_object_name = "ingredient"

    def get_success_url(self):
        return reverse_lazy("ingredients:update", kwargs={"pk": self.kwargs.get("pk")})


class IngredientCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "ingredients/update.html"
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("ingredients:list")
    success_message = "Ингредиент успешно добавлен."


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = reverse_lazy("ingredients:list")

    def get(self, request, *args, **kwargs):
        ingredient = self.get_object()
        messages.success(request, f"Ингредиент \"{ingredient.name}\" удален.")
        return self.delete(request, *args, **kwargs)
