# Generated by Django 4.1.4 on 2022-12-28 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzasite', '0004_price_remove_pizza_dough_remove_pizza_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='default_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
