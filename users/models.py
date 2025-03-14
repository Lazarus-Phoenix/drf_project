from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="почта", help_text="Укажите свой email"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите номер телефона",
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите ваш город",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
