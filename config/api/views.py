from django.shortcuts import render
from rest_framework import generics 
from pizzasite.models import Pizza
from .serializers import PizzaSerializer



class PizzaAPIView(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
