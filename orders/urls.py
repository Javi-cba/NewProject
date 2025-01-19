from django.urls import path 
from .views import createOrder,getOrders,updateStausOrder

urlpatterns = [
    path('get-orders/', getOrders, name='get-orders'), 
    path('create-order/', createOrder, name='create-order'), 
    path('status-order/', updateStausOrder, name='status-order'), 
]