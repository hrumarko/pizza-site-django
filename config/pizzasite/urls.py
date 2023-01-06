from django.urls import path 
from .views import index, res, made_order, add_case_in_cart, update_case_in_cart, delete_case_from_cart

urlpatterns = [
    path('', index, name='home'),
    path('res/', res, name='res'),
    path('cart/', add_case_in_cart, name="cart"),
    path('order/', made_order, name='order'),
    path('update-cart/', update_case_in_cart, name='update_cart'),
    path('delete-cart/', delete_case_from_cart, name='delete_cart'),
    # path('register/', UserRegister.as_view(), name='register'),
]
