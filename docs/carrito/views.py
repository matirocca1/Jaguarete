from django.shortcuts import render
from .carrito import Carro
from productos.models import Productos
from django.shortcuts import redirect
from django.views.generic.list import ListView

class Carrito(ListView):
    template_name="carrito.html"
    model=Productos
    
def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect ("carrito")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect ("carrito")


def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect ("carrito")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect ("carrito")