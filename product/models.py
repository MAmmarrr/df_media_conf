from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255,blank=True)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True,null=True)
    def __str__(self):
        return self.name
