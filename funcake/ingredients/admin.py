from django.contrib import admin
from .models import Measurement, Ingredient, IngredientConsistency


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):

    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):

    list_display = ["name", "price"]
    search_fields = ["name"]


@admin.register(IngredientConsistency)
class IngredientConsistencyAdmin(admin.ModelAdmin):

    list_display = ["name", "qty"]
    search_fields = ["ingredient__name"]
