from pizzasite.models import Pizza, Price, Dough
from rest_framework import serializers


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['price', 'radius']


class DoughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dough
        fields = ['name', 'additional_payment']


class PizzaSerializer(serializers.ModelSerializer):
    price = PriceSerializer(many=True, read_only=True)
    dough = DoughSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pizza
        fields = ['name', 'price', 'dough', 'default_price', 'image']

