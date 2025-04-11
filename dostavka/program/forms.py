from django import forms
from .models import Menu, Dish, Order, Client, OrderDish
from django.core.validators import RegexValidator


class MenuForm(forms.ModelForm):
    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Menu
        fields = ['date', 'dishes']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }


class OrderForm(forms.ModelForm):
    client_phone = forms.CharField(
        label='Телефон клиента',
        max_length=15,
        widget=forms.TextInput(attrs={'autocomplete': 'off'}),
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Номер телефона должен быть в формате: '+79991234567'"
            )
        ]
    )

    class Meta:
        model = Order
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3})
        }


class OrderDishForm(forms.ModelForm):
    class Meta:
        model = OrderDish
        fields = ['dish', 'quantity']
