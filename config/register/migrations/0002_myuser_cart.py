# Generated by Django 4.1.4 on 2022-12-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzasite', '0001_initial'),
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='cart',
            field=models.ManyToManyField(to='pizzasite.pizza'),
        ),
    ]