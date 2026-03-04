from django.contrib import admin

from .models import Song,Movie, Person, Role,SongArtists

admin.site.register(Song)
admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(SongArtists)
# python manage.py createsuperuser

