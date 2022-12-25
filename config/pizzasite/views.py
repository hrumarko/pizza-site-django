from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza
from .forms import RegistrationUserForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


def index(request):
    """Return first page woth all pizzas"""
    objs = Pizza.objects.all()
    ctx = {
        'objs': objs,
    }
    print(objs)
    return render(request, 'pizzasite/base.html', ctx)


class UserRegister(CreateView):
    form_class = RegistrationUserForm
    template_name = 'pizzasite/register.html'

    def get_success_url(self):
        return HttpResponse("Succes")
