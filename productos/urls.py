# productos/urls.py
from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.home, name='home'), 
    path('buscar/', views.buscar_productos, name='buscar_productos'), # nombre 'buscar_productos' usado en templates  
]

