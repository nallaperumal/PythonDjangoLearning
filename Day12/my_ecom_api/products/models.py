from django.db import models
class Product(models.Model):
  Name = models.CharField(max_length=55)
  Price = models.FloatField()
  Desc = models.CharField(max_length=10)
# python manage.py makemigrations products
# python manage.py migrate products
# python manage.py shell

# >>> from products.models import Product
# >>> Product.objects.all()
# >>> vanilla =  Product(Name="Vanilla Cake", Price = 3, Desc="Fresh Cake")
# >>> vanilla.save()
# >>> Product.objects.all()
# >>> Product.objects.all().values()