# Generated by Django 4.1.4 on 2022-12-26 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzasite', '0002_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='pizza',
        ),
        migrations.AddField(
            model_name='cart',
            name='pizza',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pizzasite.pizza'),
        ),
    ]
