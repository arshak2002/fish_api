from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fish(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=25)
    weight = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self) :
        return self.name
