from django.contrib import admin
from .models import Pizza, Dough, Radius, Ingridients


admin.site.register(Pizza)
admin.site.register(Radius)
admin.site.register(Dough)
admin.site.register(Ingridients)
