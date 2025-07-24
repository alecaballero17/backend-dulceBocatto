from django.db import models
from django.db.models import Sum, F

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_total(self):
        detalles = self.detalles.select_related('producto')
        total = sum(detalle.cantidad * detalle.producto.precio for detalle in detalles)
        self.total = total
        self.save(update_fields=['total'])

    def __str__(self):
        return f'Pedido {self.id} de {self.cliente.nombre}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.pedido.calcular_total()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.pedido.calcular_total()

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} (Pedido {self.pedido.id})'
