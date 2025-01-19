from rest_framework import serializers
from .models import Order, DetOrder

class DetOrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = DetOrder
        fields = ('id', 'product_name', 'quantity','subtotal', 'price')


class OrderSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)
    details = DetOrderSerializer(source='detorder_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'client', 'client_name', 'observation', 'status', 'details','total', 'created_at')
        read_only_fields = ('created_at',)