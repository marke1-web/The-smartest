from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомная модель пользователя."""

    GENDER_CHOICES = [("М", "Мужчина"), ("Ж", "Женщина")]
    first_name = models.CharField(
        max_length=20, verbose_name="Введите ваше имя"
    )
    first_name = models.CharField(
        max_length=20, verbose_name="Введите ваше имя"
    )
    last_name = models.CharField(
        max_length=20, verbose_name="Введите вашу фамилию"
    )
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        verbose_name="Введите ваш пол",
        null=True,
    )
    password = models.CharField(verbose_name='Пароль', max_length=150)
    email = models.EmailField(
        max_length=254, verbose_name="Адрес электронной почты"
    )
    image = models.ImageField(
        upload_to="users/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Фотография",
    )
    date_birth = models.DateTimeField(
        verbose_name="Дата рождения", null=True, blank=True
    )

    class Meta:
        ordering = ["-first_name"]

    def __str__(self):
        """Строка для представления объекта User(в админ панели)"""
        return f"{self.first_name} {self.last_name}"
