from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Кастомная модель пользователя."""

    GENDER_CHOICES = [("М", "Мужчина"), ("Ж", "Женщина")]

    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        verbose_name="Пол",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="users/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Фотография",
    )
    date_birth = models.DateField(
        verbose_name="Дата рождения", null=True, blank=True
    )

    def __str__(self):
        """Строка для представления объекта User(в админ панели)"""
        return f"{self.username}"

    class Meta:
        ordering = ["-username"]
