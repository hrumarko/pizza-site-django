from django.urls import path
from .views import PizzaAPIView


urlpatterns = [
    path('api/all-pizzas/', PizzaAPIView.as_view(), name='api-all-pizzas')    
]
