from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(required=False)
    gender = forms.ChoiceField(
        choices=CustomUser.GENDER_CHOICES, required=False
    )
    nickname = forms.CharField(max_length=255, required=False)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'birth_date',
            'gender',
            'nickname',
        )
