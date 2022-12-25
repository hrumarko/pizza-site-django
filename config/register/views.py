from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import MyUser

def index(request):
    users = MyUser.objects.all()
    
    ctx = {
            'users': users,      
    }
    return render(request, 'register/index.html', ctx)

class UserRegister(CreateView):
    form_class = UserRegisterForm
    template_name = 'register/registr.html'

    def get_success_url(self):
        username = self.request.POST.get('email')
        password = self.request.POST.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return reverse_lazy('home')

class UserLogin(LoginView):
    template_name = 'register/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')
