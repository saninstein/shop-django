from django.forms import ModelForm, TextInput, Textarea, ChoiceField, NumberInput
from shop.models import Phone, Tablet, Notebook


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        exclude = ['link_category', 'link_items']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Например: IPhone 5',
                'class': 'new-cont-textinput',
            }),
            'video': TextInput(attrs={
                'placeholder': 'Например: https://youtu.be/lMlqg5lkWzw',
                'class': 'new-cont-textinput',
            }),
            'description': Textarea(attrs={
                'placeholder': 'Описание...',
                'class': 'new-cont-textarea',
            }),
            'price': NumberInput(attrs={
                'placeholder': '3500',
                'class': 'new-cont-textinput',
            }),
            'price_opt': NumberInput(attrs={
                'placeholder': '0',
                'class': 'new-cont-textinput',
            }),
            'diagonal': NumberInput(attrs={
                'placeholder': '5',
                'class': 'new-cont-textinput',
            }),
            'resolution': TextInput(attrs={
                'placeholder': 'Например: 1280x720',
                'class': 'new-cont-textinput',
            }),
            'display_other': TextInput(attrs={
                'placeholder': 'Например: IPS, 36K цветов...',
                'class': 'new-cont-textinput',
            }),
            'wireless': TextInput(attrs={
                'placeholder': 'Например: WIFI, 4G',
                'class': 'new-cont-textinput',
            }),
            'interfaces': TextInput(attrs={
                'placeholder': 'Например: USB, miniJack 3.5',
                'class': 'new-cont-textinput',
            }),
            'battery': NumberInput(attrs={
                'placeholder': '4200',
                'class': 'new-cont-textinput',
            }),
            'camera': NumberInput(attrs={
                'placeholder': '5',
                'class': 'new-cont-textinput',
            }),
            'camera_other': TextInput(attrs={
                'placeholder': 'Например: автофокус...',
                'class': 'new-cont-textinput',
            }),
            'front_camera': NumberInput(attrs={
                'placeholder': '5',
                'class': 'new-cont-textinput',
            }),
            'front_camera_other': TextInput(attrs={
                'placeholder': 'Например: автофокус...',
                'class': 'new-cont-textinput',
            }),
            'osystem': TextInput(attrs={
                'placeholder': 'Например: Android 5.1',
                'class': 'new-cont-textinput',
            }),
            'core_other': TextInput(attrs={
                'placeholder': 'Например: Nvidia Tegra 3',
                'class': 'new-cont-textinput',
            }),
            'ram': NumberInput(attrs={
                'placeholder': '5',
                'class': 'new-cont-textinput',
            }),
            'memory': NumberInput(attrs={
                'placeholder': '5',
                'class': 'new-cont-textinput',
            }),
            'memory_other': TextInput(attrs={
                'placeholder': 'Например: SSD',
                'class': 'new-cont-textinput',
            }),
            'other': TextInput(attrs={
                'placeholder': 'Например: Бронированный корпус',
                'class': 'new-cont-textinput',
            }),
            'standards': TextInput(attrs={
                'placeholder': 'Например: GSM 800/900/1800',
                'class': 'new-cont-textinput',
            }),

            'sim_count': NumberInput(attrs={
                'placeholder': '5',
                'class': 'new-cont-textinput',
            }),



        }
