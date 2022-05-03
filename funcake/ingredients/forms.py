from django import forms

from .models import Ingredient


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "price", "packing", "measurement")
        help_texts = {
            "name": "Название ингредиента, не более 255 символов",
            "packing": "В какой развесовке/объеме обычно покупаете",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

        self.fields["measurement"].widget.attrs.update({"class": "form-select"})

    def clean(self):
        name = self.cleaned_data.get("name", None)
        if name:
            self.cleaned_data["name"] = name.lower()
        return super().clean()
