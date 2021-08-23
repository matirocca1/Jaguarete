from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from productos.models import * 
from django.contrib.auth import get_user_model
from inicio.forms import ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

class Inicio(ListView):
    template_name = 'inicio/index.html'
    model=Productos
    user= get_user_model()

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['ultimos_tres']=Productos.objects.all().order_by('-id')[:3]
        context['ultimos_siete']=Productos.objects.all().order_by('-id')[3:10]
        return context 

class AcercaDe (TemplateView):
    template_name = 'acerca.html'

class Gracias(TemplateView):
    template_name='gracias.html'

class Contacto(FormView):
    template_name= 'contacto.html'
    form_class = ContactForm
    success_url=reverse_lazy('gracias')


    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
