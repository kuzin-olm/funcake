from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ["title", "author", "updated_at", "created_at", "is_visible"]
    list_filter = ("is_visible",)
    search_fields = ["title", "description", "text"]
