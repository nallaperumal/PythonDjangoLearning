# python manage.py createsuperuser

from django.contrib import admin

from .models import BoxOfficeCollection, Movie, Product, Sales

admin.site.register(Product)
admin.site.register(Movie)
admin.site.register(Sales)
admin.site.register(BoxOfficeCollection)


# python manage.py makemigrations products
# python manage.py migrate products