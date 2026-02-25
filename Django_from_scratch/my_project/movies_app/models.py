from django.db import models
from rest_framework import serializers

    
class Movie(models.Model):
    name = models.CharField(max_length=20)
    lang = models.CharField(max_length=20)
    year_of_release = models.PositiveIntegerField()
    imdb_rating = models.FloatField()
    director = models.CharField(max_length=50, default="Cameron")

class Song(models.Model):   
    name = models.CharField(max_length=20)
    running_time = models.FloatField()
    singer = models.CharField(max_length=20)
    album = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'     

class MovieSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True, source = 'song_set')
    class Meta:
        model = Movie
        # fields = '__all__'    
        fields = ['id','name','lang', 'year_of_release','imdb_rating','director', 'songs']