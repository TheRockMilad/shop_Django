from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.PositiveIntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=60,null=True,blank=True)

    def __str__(self):
        return f"{self.name} {self.family} {self.email} {self.username}"


# -------------------------------------------------------------------------

def image_path(instance, filename):  # a.jpg
    ext = filename.split('.')[-1]  # jpg
    name = filename.split('.')[0]  # a
    current_Date = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')  # 20200415163214
    return f'images/product/{name}_{current_Date}.{ext}'  # images/product/a_20200415163214.jpg


# -------------------------------------------------------------------------


class Product(models.Model):
    name = models.CharField(max_length=200, )
    price = models.IntegerField()
    register_date = models.DateTimeField(auto_now_add=True, )
    image = models.ImageField(upload_to=image_path, default='images/product/nophoto.png')

    def __str__(self):
        return f'{self.name} {self.price}'

class ProductFeature(models.Model):
    feature_name = models.CharField(max_length=200)
    feature_value = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True,related_name='features')
    user_register = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
