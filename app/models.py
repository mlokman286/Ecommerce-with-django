from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Catagory(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Sub_Catagory(models.Model):
    name = models.CharField(max_length=150)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name    

class Product(models.Model):
    availability =(('in stock','IN STOCK'),('out of stock','OUT OF STOCK')) 

    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE,null = False,default='')
    sub_catagory=models.ForeignKey(Sub_Catagory,on_delete=models.CASCADE,null = False,default='')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null= True)
    image = models.ImageField(upload_to='ecommerce/pimg',null = True, blank=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    availability = models.CharField(choices = availability,null = True,max_length = 200)
    date=models.DateField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name
    
class ContacUs(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=300)
    message=models.TextField()
    def __str__(self):
        return self.name
    
class Order(models.Model):
    image = models.ImageField(upload_to='ecommerce/order/images')
    product =models.CharField(max_length=1000,default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.CharField(max_length=5)
    total = models.CharField(max_length=1000,default='')
    address = models.TextField()
    phone = models.CharField(max_length=15)
    pincode = models.CharField(max_length=8)
    date = models.DateField(default=datetime.datetime.today)
    def __str__(self):
        return self.product