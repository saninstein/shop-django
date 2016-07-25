from django.forms import ModelForm, TextInput, Textarea, EmailInput, HiddenInput, NumberInput
from shop.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['items']
        widgets = {
            'email': EmailInput(attrs={
                'placeholder': 'Введите адрес',
                'class': 'new-cont-textinput',
            }),
            'phone': NumberInput(attrs={
                'placeholder': 'Введите номер',
                'class': 'new-cont-textinput',
            }),
            'message': Textarea(attrs={
                'placeholder': 'Текст сообщения',
                'class': 'new-cont-textarea',
            }),
        }
