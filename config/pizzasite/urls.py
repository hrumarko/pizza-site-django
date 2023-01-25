from django.urls import path 
from .views import index, made_order, add_case_in_cart, update_case_in_cart, delete_case_from_cart, result_order, orders

urlpatterns = [
    path('', index, name='home'),
    path('cart/', add_case_in_cart, name="cart"),
    path('order/', made_order, name='order'),
    path('update-cart/', update_case_in_cart, name='update_cart'),
    path('delete-cart/', delete_case_from_cart, name='delete_cart'),
    path('result-order/', result_order, name='result_order'),
    path('orders/', orders, name='orders')
    # path('register/', UserRegister.as_view(), name='register'),
]
