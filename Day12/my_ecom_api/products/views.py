from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Product, Sales
from .serializers import ProductSerializer, SalesSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow anyone to view products
            permission_classes = [AllowAny]
        else:
            # Require authentication for POST, PUT, DELETE
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

def products(request):
    return HttpResponse("Hello world! Welcome to products")
def product_json(request):
    # In a real application, you would fetch product details from a database
    allProducts = Product.objects.all().values()
    return JsonResponse(list(allProducts), safe=False)

def product_json_detail(request, product_id):
    product_details = [
        {"id": 1, "name": "Banana Cake", "price": 10.99, "description": "with ripe bananas."},
        {"id": 2, "name": "Coffee Cake", "price": 19.99, "description": "Rich coffee cake"},
        {"id": 3, "name": "Vanilla Cake", "price": 5.99, "description": "classic vanilla cake"},
    ]
    if product_id >= len(product_details):
        return JsonResponse({"error": "Product not found"}, status=404)
    product = product_details[product_id]
    return JsonResponse(product,safe=False)

@api_view(['GET'])
def get_products(request):
    allProducts = Product.objects.all().values()
    serializer = ProductSerializer(Product.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)