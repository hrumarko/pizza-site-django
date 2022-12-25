from django.urls import path 
from .views import index 


urlpatterns = [
    path('', index, name='home'),
    # path('register/', UserRegister.as_view(), name='register'),
]
