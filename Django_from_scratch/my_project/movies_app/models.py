from django.db import models
from rest_framework import serializers

class Movie(models.Model):
    name = models.CharField(max_length=20)
    lang = models.CharField(max_length=20)
    year_of_release = models.PositiveIntegerField()
    imdb_rating = models.FloatField()
    director = models.CharField(max_length=50, default="Cameron")

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'    
    