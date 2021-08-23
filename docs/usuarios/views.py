from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import  LoginView
from django.urls import reverse_lazy
from django.views import generic



class Registro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registro.html'


class Login(LoginView):
    template_name='login.html'
    authentication_form= AuthenticationForm
    success_url = reverse_lazy('inicio')
