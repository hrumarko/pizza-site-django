# Generated by Django 4.1.4 on 2023-01-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzasite', '0017_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='commentary',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='is_finished',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
