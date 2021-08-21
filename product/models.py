from django.db import models
# Create your models here.

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    name = models.IntegerField()

class NewProduct(models.Model):
    name = models.CharField(max_length=255,blank=True)
    price = models.IntegerField(blank=True)
    description = models.CharField(max_length=255,blank=True)
    image = models.URLField(blank=True)