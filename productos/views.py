from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Producto, Carrito


# 🏠 Página de inicio
def home(request):
    return render(request, 'productos/home.html')


# 🛍️ Catálogo de productos (visible solo para usuarios autenticados)
@login_required
def catalogo(request):
    categoria = request.GET.get('categoria')
    if categoria:
        productos = Producto.objects.filter(categoria=categoria)
    else:
        productos = Producto.objects.all()

    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.subtotal for item in carrito_items)

    return render(request, 'productos/catalogo.html', {
        'productos': productos,
        'carrito_items': carrito_items,
        'categoria_actual': categoria,
        'total': total
    })


# 🔍 Buscar productos
def buscar_productos(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'productos/catalogo.html', {
        'productos': productos,
        'query': query
    })


# 🟢 Agregar producto al carrito (normal)
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, creado = Carrito.objects.get_or_create(usuario=request.user, producto=producto)
    if not creado:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('productos:catalogo')


# 🟣 Agregar producto al carrito con AJAX (sin recargar página)
@login_required
def agregar_al_carrito_ajax(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, creado = Carrito.objects.get_or_create(usuario=request.user, producto=producto)

    if not creado:
        carrito_item.cantidad += 1
        carrito_item.save()

    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.subtotal for item in carrito_items)

    return JsonResponse({
        'nombre': producto.nombre,
        'cantidad': carrito_item.cantidad,
        'total': total,
    })


# 🧾 Ver carrito (solo si quisieras una vista aparte)
@login_required
def ver_carrito(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.subtotal for item in carrito_items)

    return render(request, 'productos/catalogo.html', {
        'productos': Producto.objects.all(),
        'carrito_items': carrito_items,
        'total': total
    })


# 📋 Resumen del pedido
@login_required
def resumen_pedido(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    subtotal = sum(item.subtotal for item in carrito_items)
    envio = 8000 if subtotal > 0 else 0
    total = subtotal + envio

    return render(request, 'productos/resumen_pedido.html', {
        'carrito_items': carrito_items,
        'subtotal': subtotal,
        'envio': envio,
        'total': total
    })


# ♻️ Actualizar cantidades o eliminar productos
@login_required
def actualizar_carrito(request, item_id, accion):
    item = get_object_or_404(Carrito, id=item_id, usuario=request.user)

    if accion == 'sumar':
        item.cantidad += 1
        item.save()

    elif accion == 'restar':
        if item.cantidad > 1:
            item.cantidad -= 1
            item.save()
        else:
            item.delete()

    elif accion == 'eliminar':
        item.delete()

    return redirect('productos:resumen_pedido')

@login_required
def agregar_al_carrito_ajax(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, creado = Carrito.objects.get_or_create(usuario=request.user, producto=producto)

    if not creado:
        carrito_item.cantidad += 1
        carrito_item.save()

    # Obtenemos los productos actuales del carrito
    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.subtotal for item in carrito_items)

    # Creamos una lista con los productos para actualizar el carrito lateral
    carrito_data = [
        {"nombre": item.producto.nombre, "cantidad": item.cantidad}
        for item in carrito_items
    ]

    return JsonResponse({
        "ok": True,
        "nombre": producto.nombre,
        "cantidad": carrito_item.cantidad,
        "total": total,
        "carrito": carrito_data
    })
@login_required
def pago(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    subtotal = sum(item.subtotal for item in carrito_items)
    envio = 8000 if subtotal > 0 else 0
    total = subtotal + envio

    if request.method == "POST":
        # Aquí podrías integrar una pasarela de pago real (PayU, MercadoPago, Stripe, etc.)
        # Por ahora solo simulamos que el pedido se realizó correctamente.
        carrito_items.delete()
        return render(request, 'productos/pago_exitoso.html', {'total': total})

    return render(request, 'productos/pago.html', {
        'carrito_items': carrito_items,
        'subtotal': subtotal,
        'envio': envio,
        'total': total
    })


