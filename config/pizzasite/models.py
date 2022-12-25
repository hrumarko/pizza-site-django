from django.db import models


class Pizza(models.Model):
    image = models.ImageField(upload_to="photos/")
    name = models.CharField(max_length=20)
    radius = models.ManyToManyField('Radius')
    dough = models.ManyToManyField('Dough')
    price = models.DecimalField(decimal_places=0, max_digits=2)
    ingridients = models.ManyToManyField('Ingridients')


class Radius(models.Model):
    size = models.SmallIntegerField()

    def __str__(self):
        return str(self.size)


class Dough(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Ingridients(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
