from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from .models import Order, DetOrder
from products.models import Product
from clients.models import Client
from .serializers import OrderSerializer

@csrf_exempt
@api_view(['GET'])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def createOrder(request):
    try:
        data = json.loads(request.body)

        # Verifica si los datos necesarios están presentes
        client_id = data.get('client_id')
        observation = data.get('observation', '')
        details = data.get('details', [])  

        if not client_id or not details:
            return Response({'error': 'Client ID and order details are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Verifica que el cliente existe
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return Response({'error': 'Client not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Crea la orden (encabezado)
        order = Order.objects.create(client=client, observation=observation)
        total = 0
      
        # Crear los detalles de la orden
        for detail in details:
            product_id = detail.get('product_id')
            quantity = detail.get('quantity', 0)

            # Verificamos que el producto existe
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({'error': f'Product with ID {product_id} not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Verifica que la cantidad sea válida
            if quantity <= 0:
                return Response({'error': f'Invalid quantity for product ID {product_id}.'}, status=status.HTTP_400_BAD_REQUEST)

            # Creamos el detalle
            DetOrder.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price,
                subtotal=product.price * quantity
            )

            total += product.price * quantity

        # Actualizar el total de la orden
        order.total = total
        order.save()

        return Response({'message': 'Order created successfully!', 'order_id': order.id}, status=status.HTTP_201_CREATED)
    
    except json.JSONDecodeError:

        return Response({'error': 'Invalid JSON payload.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:

        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['PATCH'])
def updateStausOrder(request):
    try:
        data = json.loads(request.body)

        order_id = data.get('order_id')
        order_status = data.get('status')

        if not order_id or not order_status:
            return Response({'error': 'Order ID and status are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)


        order.status = order_status
        order.save()

        return Response({'message': 'Order updated successfully!'}, status=status.HTTP_200_OK)

    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON payload.'}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

