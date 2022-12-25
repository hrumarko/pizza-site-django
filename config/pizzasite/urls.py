from django.urls import path 
from .views import index, UserRegister


urlpatterns = [
    path('', index, name='home'),
    path('register/', UserRegister.as_view(), name='register'),
]
