from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=200)
    img= models.ImageField(upload_to='pics')
    price= models.IntegerField()
    discription=models.TextField()
    delivertime=models.CharField(max_length=400)
    delivering=models.CharField(max_length=400)



class Cart(models.Model):
    users=models.IntegerField()
    products=models.IntegerField()