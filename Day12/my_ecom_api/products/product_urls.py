from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/json/', views.product_json, name='product_json'),
    path('products/json/<int:product_id>/', views.product_json_detail, 
                name='product_json_detail'),

    path('api/products/', views.get_products, name='get_products'),      

     path('api/products/add/', views.add_product, name='add_product')      
]