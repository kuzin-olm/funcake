from django.db import models
from django.urls import reverse


class Measurement(models.Model):
    """
    Единицы измерения фасовки
    """
    class Mete:
        ordering = ["-name"]

    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return f"{self.name}"


class Ingredient(models.Model):
    """
    Базовый ингредиент
    """
    class Meta:
        ordering = ["-name"]

    name = models.CharField("Название ингредиента", max_length=255, unique=True)
    price = models.FloatField("Цена")
    packing = models.FloatField("Фасовка")

    measurement = models.ForeignKey(Measurement, on_delete=models.PROTECT)

    def __str__(self):
        return f"Ингредиент \"{self.name}\" ({self.packing} {self.measurement.name}.) по {self.price} руб."


class IngredientConsistency(models.Model):
    """
    Консистенция ингредиента
    """
    class Meta:
        ordering = ["-ingredient__name"]

    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    qty = models.FloatField("Количество")

    @property
    def name(self):
        return self.ingredient.name

    def __str__(self):
        return f"Консистенция \"{self.ingredient.name}\" {self.qty} {self.ingredient.measurement}."
