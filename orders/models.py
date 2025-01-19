from django.db import models
from clients.models import Client
from products.models import Product
# Create your models here.

class Order( models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    observation = models.TextField()
    status = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('Enviado', 'Enviado'), ('Entregado', 'Entregado')] ,default='Pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class DetOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)