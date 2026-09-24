from django import forms

from catalog.models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования продукта."""

    def __init__(self, *args, **kwargs):
        """Добавляет стили к полям формы."""
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price")

    def clean_name(self):
        """Проверяет название на запрещенные слова."""
        name = self.cleaned_data["name"].lower()

        for word in FORBIDDEN_WORDS:
            if word in name:
                raise forms.ValidationError("Название содержит запрещенное слово.")

        return name

    def clean_description(self):
        """Проверяет описание на запрещенные слова."""
        description = self.cleaned_data["description"].lower()

        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError("Описание содержит запрещенное слово.")

        return description

    def clean_price(self):
        """Проверяет, что цена не отрицательная."""
        price = self.cleaned_data["price"]

        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")

        return price
