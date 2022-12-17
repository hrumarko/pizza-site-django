from django.db import models


class Pizza(models.Model):
   image = models.ImageField(upload_to="photos/")
   name = models.CharField(max_length=20)
   radius = models.ManyToManyField('Radius')  # add model with radius(smallinteger)
   dough = models.ManyToManyField('Dough')# add model with doughs(char)
   price = models.DecimalField(decimal_places=0, max_digits=2)
   ingridients = models.ManyToManyField('Ingridients')# add model with inrs(char)



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
