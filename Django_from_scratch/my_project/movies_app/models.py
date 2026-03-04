from django.db import models
from rest_framework import serializers

class Person(models.Model):
    name = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

class Role(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)    
    
class Movie(models.Model):
    name = models.CharField(max_length=20)
    lang = models.CharField(max_length=20)
    year_of_release = models.PositiveIntegerField()
    imdb_rating = models.FloatField()
    director = models.CharField(max_length=50, default="Cameron")

class Song(models.Model):   
    name = models.CharField(max_length=20)
    running_time = models.FloatField()
    # singer = models.CharField(max_length=20)
    artists = models.ManyToManyField(Person, through='SongArtists')
    album = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)

# through table
class SongArtists(models.Model):   
    person = models.ForeignKey(Person, on_delete=models.CASCADE) #3
    song = models.ForeignKey(Song, on_delete=models.CASCADE) # 2
    role = models.ForeignKey(Role, on_delete=models.CASCADE) #1
    class Meta:
        unique_together = ('person', 'song', 'role') 

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__' 

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__' 

class SongArtistSerializer(serializers.ModelSerializer):  
    person_name = serializers.ReadOnlyField(source ='person.name')  
    role_name = serializers.ReadOnlyField(source ='role.name')    
    class Meta:
        model = SongArtists
        fields = ['person_name','role_name']  

class SongSerializer(serializers.ModelSerializer):
    artists = SongArtistSerializer(many=True, read_only=True, source = 'songartists_set' )
    class Meta:
        model = Song
        # fields = '__all__' 
        fields = ['id','name','running_time', 'album', 'artists']    


class MovieSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True, source = 'song_set')
    class Meta:
        model = Movie
        # fields = '__all__'    
        fields = ['id','name','lang', 'year_of_release','imdb_rating','director', 'songs']