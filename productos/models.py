from django.db import models
from django.conf import settings
class Producto(models.Model):
    CATEGORIAS = [
        ('vapers', 'Vapers'),
        ('liquidos', 'Líquidos'),
        ('pods', 'Pods'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.URLField()  # usamos URL porque las imágenes son de internet
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='vapers')

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.usuario.username} - {self.producto.nombre} ({self.cantidad})"

    @property
    def subtotal(self):
        return self.cantidad * self.producto.precio