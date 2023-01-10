from django.db import models
from django.utils import timezone
from config.settings import AUTH_USER_MODEL as User


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    price = models.ManyToManyField('Price')
    default_price = models.IntegerField()  # equals price for 30cm pizza
    image = models.ImageField(upload_to="photos/")
    dough = models.ManyToManyField('Dough')

    def __str__(self):
        return self.name


class Price(models.Model):
    name_of_pizza = models.CharField(max_length=50)
    radius = models.IntegerField()
    price = models.IntegerField()
    
    class Meta:
        ordering = ['name_of_pizza', 'radius']
    
    def __str__(self):
        return f'{self.name_of_pizza} - {self.radius} = {self.price}'
    

class Dough(models.Model):
    name = models.CharField(max_length=50)
    additional_payment = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    session_id = models.CharField(max_length=255, blank=True)
    pizza = models.CharField(max_length=255)
    radius = models.CharField(max_length=255)
    dough = models.CharField(max_length=255)
    count = models.IntegerField()
    price = models.CharField(max_length=255)
    img = models.ImageField()
    main_price = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.pizza} - {self.count}'


class SessionUser(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    price = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.session_id[-5:]} = {self.price}'


class Order(models.Model):
    order = models.JSONField()
    price = models.CharField(max_length=255)
    name= models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    commentary = models.CharField(max_length=255)
    is_finished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
