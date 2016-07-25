from django.forms import ModelForm, TextInput, Textarea, EmailInput, HiddenInput
from shop.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, items):
        super(OrderForm, self).__init__(items)
        self.items = items

    widgets = {
        'email': EmailInput(attrs={
            'placeholder': 'Введите адрес',
            'class': 'new-cont-textinput',
        }),
        'phone': TextInput(attrs={
            'placeholder': 'Введите адрес',
            'class': 'new-cont-textinput',
        }),
        'message': Textarea(attrs={
            'placeholder': 'Описание...',
            'class': 'new-cont-textarea',
        }),
        'items': HiddenInput()
    }
