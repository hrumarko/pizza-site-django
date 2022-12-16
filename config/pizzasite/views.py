from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza


def index(request):
    objs = Pizza.objects.all()
    ctx = {
        'objs': objs,
    }
    print(objs)
    return render(request, 'pizzasite/base.html', ctx)
