# Generated by Django 4.1.4 on 2023-01-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzasite', '0014_alter_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
    ]
