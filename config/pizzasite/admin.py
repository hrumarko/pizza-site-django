from django.contrib import admin
from .models import Pizza, Price, Dough, Cart, SessionUser, Order


admin.site.register(Pizza)
admin.site.register(Price)
admin.site.register(Dough)
admin.site.register(Cart)
admin.site.register(SessionUser)
admin.site.register(Order)
