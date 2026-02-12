# python manage.py createsuperuser

from django.contrib import admin

from .models import Movie, Product, Sales

admin.site.register(Product)
admin.site.register(Movie)
admin.site.register(Sales)


# python manage.py makemigrations products
# python manage.py migrate products