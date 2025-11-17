# productos/urls.py
from django.urls import path
from . import views

app_name = 'productos'


urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('agregar_ajax/<int:producto_id>/', views.agregar_al_carrito_ajax, name='agregar_al_carrito_ajax'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('resumen/', views.resumen_pedido, name='resumen_pedido'),
    path('actualizar_carrito/<int:item_id>/<str:accion>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('pago/', views.pago, name='pago'),
    path('pago_exitoso/', views.pago_exitoso, name='pago_exitoso'),

]



