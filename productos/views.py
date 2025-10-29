from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.all()[:4]  # solo mostrar algunos
    return render(request, 'productos/home.html', {'productos': productos})

def buscar_productos(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'productos/resultados_busqueda.html', {
        'query': query,
        'productos': productos
    })

