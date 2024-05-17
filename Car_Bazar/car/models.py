from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
# Create your models here.

class Add_Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_price = models.IntegerField()
    car_quantity = models.IntegerField()
    car_details = models.TextField()
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="car_brand")
    car_image = models.ImageField(upload_to='uploads/', blank=True,  null=True)
    buyer = models.ManyToManyField(User, blank=True)
    def __str__(self):
        return self.car_name
    
    
