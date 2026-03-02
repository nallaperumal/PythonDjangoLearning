from django.contrib import admin

from .models import Song,Movie

admin.site.register(Song)
admin.site.register(Movie)
# python manage.py createsuperuser

