from django import forms
from .models import User
from django.core.exceptions import ValidationError


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'gender',
            'email',
            'date_birth',
        ]


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        label='Подтверждение пароля', widget=forms.PasswordInput
    )
    gender = forms.ChoiceField(
        label='Пол', choices=[('M', 'Мужской'), ('F', 'Женский')]
    )
    email = forms.EmailField(label='Email')
    date_birth = forms.DateField(label='Дата рождения')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise ValidationError("Пароль и подтверждение пароля не совпадают")
