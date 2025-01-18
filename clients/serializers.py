from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields = ('id','name','email','password','is_activated','created_at')
        read_only_fields=('created_at',)