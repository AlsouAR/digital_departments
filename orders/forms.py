import re
from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    requires_delivery = forms.ChoiceField(
        label="Доставка",
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ],
        widget=forms.RadioSelect)
    
    address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        label="Оплата наличными",
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ],
        widget=forms.RadioSelect)

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")
        
        pattern = re.compile(r'\+?1?\d{9,15}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data
