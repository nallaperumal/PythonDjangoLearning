from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

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