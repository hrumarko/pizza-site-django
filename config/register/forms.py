from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.core.exceptions import ValidationError
from .models import MyUser
from . import validators


class UserRegisterForm(UserCreationForm):
    name = forms.CharField(
            max_length=20,
            label='Name',
            widget=forms.TextInput(
                attrs={
                    'class': 'register-field'
                    }))
    
    email = forms.EmailField(
            label='Email',
            widget=forms.TextInput(
                attrs={
                    'class': 'register-field'
                    }))

    
    number = forms.CharField(
            max_length=20,
            label='Number',
            widget=forms.TextInput(
                attrs={
                    'placeholder': '  0XXXXXXXXX',
                    'class': 'register-field'
                    }))

    
    password1 = forms.CharField(
            label='Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'register-field'
                    }))

    
    password2 = forms.CharField(
            label='Confirm password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'register-field'
                    }))
    
    def clean_number(self):
        data = self.cleaned_data['number']
        if not validators.number_validate(data):
            raise ValidationError('Input number in correct format')
        return data

    class Meta:
        model = MyUser
        fields = ('name', 'email', 'number', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(label="Login", widget=forms.TextInput(
        attrs={
            'class': 'login-username',
            'placeholder': '  Input email or number',
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'login-password',
            }
        ))
