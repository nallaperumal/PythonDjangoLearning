---
title: markmap
markmap:
  initialExpandLevel : 2
---
# Building django from scratch
## Project and App creation (only one time)
### Git config (optional)
```sh
git config --global user.name "Your Name"
git config --global user.email "Your Mail"
```
### Virtual env creation (optional)
```sh
python -m venv myDjangoEnv
source myDjangoEnv/bin/activate
myDjangoEnv\Scripts\activate.ps1 (for windows)
```
### install packages
```sh
pip install django
pip install djangorestframework
pip install drf-spectacular
```


### Create Project
```sh
django-admin startproject my_project
```
```sh
my_project/
├── manage.py
└── my_project/
    ├── __init__.py
    └── asgi.py
    └── settings.py
    └── urls.py
    └── wsgi.py
```
- settings.py
```sh
# command to check the installed packages 
pip list
```
```py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_spectacular',
]
```
```sh
cd my_project
python manage.py runserver
```
### Create Application
```sh
python manage.py startapp movies_app
```
```sh
my_project/
├── manage.py
├── my_project/
└── movies_app/
    ├── migrations/
    └── __init__.py
    └── admin.py
    └── apps.py
    └── models.py
    └── tests.py
    └── views.py
└── manage.py    
└── db.sqlite3    
```
```py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_spectacular',
    'movies_app'
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```
## Movie Viewset creation
### Model Creation
```py
class Movie(models.Model):
    name = models.CharField(max_length=20)
    lang = models.CharField(max_length=20)
    year_of_release = models.PositiveIntegerField()
    imdb_rating = models.FloatField()
```
### Serializer
```py
from rest_framework import serializers
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'    
```
### Viewset
```py
from rest_framework import viewsets
from rest_framework.decorators import action
from my_project.movies_app.models import Movie, MovieSerializer

# ViewSet for API endpoints
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```
### Perform migration
```sh
python manage.py makemigrations
python manage.py migrate
```
### URLs configuration
```py
from django.urls import path, include
from movies_app import views
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.views.generic import RedirectView

router = DefaultRouter()
router.register(r'api/movies', views.MovieViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('', RedirectView.as_view(url='/api/docs/')),
    path('admin/', admin.site.urls), 
    path('api/schema/', 
        SpectacularAPIView.as_view(), 
        name='schema'),
    path('api/docs/', 
        SpectacularSwaggerView.as_view(url_name='schema'), 
        name='swagger-ui'),
]
```
## Queryset samples
### top 3 movies
```py
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    @action(detail=False, methods=['get'])
    def top_3_movies(self, request):
        movies = Movie.objects.order_by('-imdb_rating')[:3]
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)
```
### Only good movies
```py
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
        movies = Movie.objects.filter(imdb_rating__gte=8.0).order_by('-imdb_rating')
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)
```

