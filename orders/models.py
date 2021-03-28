from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  customercode = models.CharField(max_length=20)


class Order(models.Model):
  reference = models.CharField(max_length=50)
  date = models.DateField(auto_now=False, auto_now_add=True)
  business_partner = models.CharField(max_length=20)
  billing_street = models.CharField(max_length=50)
  billing_zipcode = models.CharField(max_length=20)
  billing_city = models.CharField(max_length=50)
  billing_country = models.CharField(max_length=10)
  shipping_name = models.CharField(max_length=20)
  shipping_street = models.CharField(max_length=50)
  shipping_zipcode = models.CharField(max_length=20)
  shipping_city = models.CharField(max_length=50)
  shipping_country = models.CharField(max_length=10)
  external_reference = models.CharField(max_length=10)

  def __str__(self):
    return self.id


class Items(models.Model):
  productcode = models.CharField(max_length=20)
  quantity = models.DecimalField(max_digits=7, decimal_places=2)
  reference = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=7,decimal_places=2)
  amount = models.DecimalField(max_digits=7,decimal_places=2)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)

  def __str__(self):
    return self.id