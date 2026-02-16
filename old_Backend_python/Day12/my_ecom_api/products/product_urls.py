from django.urls import path, include
from rest_framework.routers import DefaultRouter
# http://127.0.0.1:8000/api/docs/
from . import views

router = DefaultRouter()
router.register(r'api/products', views.ProductViewSet)
router.register(r'api/sales', views.SalesViewSet)
router.register(r'api/movies', views.MovieViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('movies/', views.hello_movies, name='hello_movies'),
    path('products/', views.products, name='products'),
    path('products/json/', views.product_json, name='product_json'),
    path('products/json/<int:product_id>/', views.product_json_detail, 
                name='product_json_detail'),

    path('api/products/', views.get_products, name='get_products'),      

     path('api/products/add/', views.add_product, name='add_product')      
]

# pip install drf-spectacular