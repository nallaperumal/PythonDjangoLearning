from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from movies_app.models import Movie, MovieSerializer

# ViewSet for API endpoints
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=['get'])
    def top_3_movies(self, request):
        movies = Movie.objects.order_by('-imdb_rating')[:3]
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def only_good_movies(self, request):
        movies = Movie.objects.filter(imdb_rating__gt=8.0).order_by('-imdb_rating')
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)
