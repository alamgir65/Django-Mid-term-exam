from django.db import models
from car.models import Add_Car
import datetime
# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=100)
    car = models.ForeignKey(Add_Car, on_delete=models.CASCADE, related_name="comments")
    createn_on = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    

