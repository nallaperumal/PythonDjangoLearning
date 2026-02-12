from rest_framework import serializers
from .models import BoxOfficeCollection, Product,Sales, Movie

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'    

class BoxOfficeCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxOfficeCollection
        fields = '__all__'