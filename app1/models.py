from django.db import models

# Create your models here.
class Customer(models.Model):
    c_id=models.IntegerField(unique=True)
    name=models.CharField(max_length=60)
    product=models.CharField(max_length=70)
    quantity=models.IntegerField()
    price=models.FloatField()