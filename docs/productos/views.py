from .models import Productos
from django.views.generic import TemplateView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.db.models.query_utils import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#---------------------------------Camperas------------------------------------

class Remeras(TemplateView):
    context_object_name='remeras'
    template_name='remeras.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['remeras']=Productos.objects.filter(categorias_id = 1)
        return context


#---------------------------------Camperas------------------------------------

class Camperas(TemplateView):
    context_object_name='camperas'
    template_name='camperas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['camperas']=Productos.objects.filter(categorias_id = 2)
        return context


#---------------------------------Camperas------------------------------------

class Pantalones(TemplateView):
    context_object_name='pantalones'
    template_name='pantalones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pantalones']=Productos.objects.filter(categorias_id = 3)
        return context

#---------------------------------Camperas------------------------------------

class Zapatillas(TemplateView):
    context_object_name='zapatillas'
    template_name='zapatillas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zapatillas']=Productos.objects.filter(categorias_id = 4)
        return context

#---------------------------------Camperas------------------------------------

class Medias(TemplateView):
    context_object_name='medias'
    template_name='medias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medias']=Productos.objects.filter(categorias_id = 5)
        return context

class ProductoDetalle(DetailView):
    model=Productos
    template_name="detalle.html"
    context_object_name='producto'

    def get_object(self):
        producto=Productos.objects.get(pk=self.kwargs['pk'])
        return producto

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['producto']=Productos.objects.get(pk=self.kwargs['pk'])
        return context

class Busqueda(ListView):
    model = Productos
    template_name = "resultados.html"
    context_object_name='productos'

    def get_queryset(self):
        query=self.request.GET.get('q')
        productos=Productos.objects.filter(
            Q(nombre__icontains=query)
        )
        return productos

class CrearProducto(CreateView):
    model= Productos
    template_name='nuevo.html'
    fields= ['nombre', 'descripcion', 'precio','categorias', 'imagen']
    success_url=reverse_lazy('inicio')

class EditarProducto(UpdateView):
    model=Productos
    template_name='editar.html'
    fields=['nombre','precio']
    success_url=reverse_lazy('inicio')

    def get_object(self):
        producto=Productos.objects.get(pk=self.kwargs['pk'])
        return producto

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['producto']=Productos.objects.get(pk=self.kwargs['pk'])
        return context

class EliminarProducto(DeleteView):
    model=Productos
    template_name='borrar.html'
    success_url=reverse_lazy('inicio')

    def get_object(self):
        producto=Productos.objects.get(pk=self.kwargs['pk'])
        return producto

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['producto']=Productos.objects.get(pk=self.kwargs['pk'])
        return context

    