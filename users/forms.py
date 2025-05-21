from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='необязательное поле')
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)  # добавили поле email
    usable_password = None

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')  # исправили на fields и добавили запятые

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр')
        return phone_number