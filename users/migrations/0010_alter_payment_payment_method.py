# Generated by Django 5.1.7 on 2025-04-07 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_alter_payment_payment_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(
                choices=[("cash", "Наличные"), ("transfer", "Перевод на счет")],
                max_length=30,
                verbose_name="метод оплаты",
            ),
        ),
    ]
