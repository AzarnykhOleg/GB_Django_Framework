from django import forms
from .models import Client, Product

# форма создания новго клиента
class ClientForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Имя",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите имя пользователя"}
        ),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "example@example.com"}
        ),
    )
    phone = forms.CharField(
        max_length=11,
        label="Телефон",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "+7(999)999-99-99 "}
        ),
    )
    address = forms.CharField(
        max_length=100,
        label="Адрес",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите адрес"}
        ),
    )

# форма создания новго товара
class ProductForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Название товара",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите название товара"}
        ),
    )
    description = forms.CharField(
        label="Описание товара",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Введите описание товара"}
        ),
    )
    price = forms.DecimalField(
        label="Цена товара",
        max_digits=100,
        decimal_places=2,
        initial=0,
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Введите цену"}
        ),
    )
    quantity = forms.IntegerField(
        label="Количество товара",
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    product_image = forms.ImageField(
        label="Изображение товара",
        widget=forms.FileInput(attrs={"class": "form-control", "type": "file"}),
    )

# форма создания новго заказа
class OrderForm(forms.Form):
    buyer = forms.ModelChoiceField(queryset=Client.objects.all())
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple
    )
