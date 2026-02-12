from django.db import models
class Product(models.Model):
  Name = models.CharField(max_length=55)
  Price = models.FloatField()
  Desc = models.CharField(max_length=10)

class Sales(models.Model):
  # Name = models.CharField(max_length=15)
  Product = models.ForeignKey(Product, on_delete=models.CASCADE)
  Quantity = models.PositiveIntegerField() 
  Country = models.CharField(max_length=100) 
  Created_at = models.DateTimeField(auto_now_add=True)

class Movie(models.Model):
    Name = models.CharField(max_length=20)
    Lang = models.CharField(max_length=20)
    Year_of_Release = models.PositiveIntegerField()
    imdb_rating = models.FloatField()

# python manage.py makemigrations products
# python manage.py migrate products
# python manage.py shell

# >>> from products.models import Product
# >>> Product.objects.all()
# >>> vanilla =  Product(Name="Vanilla Cake", Price = 3, Desc="Fresh Cake")
# >>> vanilla.save()
# >>> Product.objects.all()
# >>> Product.objects.all().values()