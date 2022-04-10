from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy

from .models import Recipe


User = get_user_model()


class RecipeListView(LoginRequiredMixin, ListView):
    template_name = "recipes/list.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user).order_by("-created_at")


class RecipeDetailView(DetailView):
    template_name = "recipes/detail.html"
    model = Recipe
    context_object_name = "recipe"


# class RecipeUpdateView(UpdateView):
#     template_name = "recipes/update.html"
#     model = Recipe
#     context_object_name = "recipe"
