from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    )

    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )
    nickname = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


CustomUser._meta.get_field('groups').remote_field.related_name = (
    'customuser_set'
)
CustomUser._meta.get_field('user_permissions').remote_field.related_name = (
    'customuser_set'
)
