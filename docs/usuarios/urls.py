from django.urls import path
from .views import Login, Registro

urlpatterns = [
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', Login.as_view(),name='login'),
]
