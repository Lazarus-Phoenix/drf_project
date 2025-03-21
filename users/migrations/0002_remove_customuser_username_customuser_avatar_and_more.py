# Generated by Django 5.1.7 on 2025-03-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="username",
        ),
        migrations.AddField(
            model_name="customuser",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите аватар",
                null=True,
                upload_to="users/avatars/",
                verbose_name="аватар",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="city",
            field=models.CharField(
                blank=True,
                help_text="Укажите ваш город",
                max_length=100,
                null=True,
                verbose_name="Город",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="Укажите номер телефона",
                max_length=15,
                null=True,
                verbose_name="Телефон",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                help_text="Укажите свой email",
                max_length=254,
                unique=True,
                verbose_name="почта",
            ),
        ),
    ]
