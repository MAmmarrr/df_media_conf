from django.db import models
from mongoengine import *
# Create your models here.
class Product(Document):
    name = StringField(required=True)
    price= StringField(required=True)
