from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.all()[:4]  # solo mostrar algunos
    return render(request, 'productos/home.html', {'productos': productos})


