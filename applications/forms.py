from django import forms
from django.contrib.auth import get_user_model
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['user', 'status']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['master'] = forms.ModelChoiceField(
            queryset=get_user_model().objects.filter(is_worker=True), label='Мастер')
