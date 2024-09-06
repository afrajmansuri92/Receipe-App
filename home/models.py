from django.db import models

class Student(models.Model):
    #id = models.autoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    # image = models.ImageField()
    # file = models.FileField()
    
 
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField()   
    
    
class Product(models.Model):
    pass

# Create your models here.
