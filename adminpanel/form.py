from django.forms import ModelForm
from shop.models import Phone, Tablet, Notebook


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        exclude = ['link_category', 'link_items']
