from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .widgets import TelInput


class RegisterForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'patronymic', 'telephone',
                  'password', 'username', 'driver_license_number', 'driver_license_series']

        widgets = {
            'telephone': TelInput(),
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        print(self.cleaned_data)
        return get_user_model().objects.create_user(**self.cleaned_data)


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    def __init__(self, request, **kwargs):
        super().__init__(**kwargs)
        self.request = request

    def clean(self):
        super().clean()

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password is not None:
            self.user = authenticate(username=username, password=password)

            if self.user is None:
                self.add_error('username', ValidationError('Пользователь не найден'))
                self.add_error('password', ValidationError('Пользователь не найден'))

        return self.cleaned_data

    def get_user(self):
        return self.user
