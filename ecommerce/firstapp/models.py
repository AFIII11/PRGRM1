from django.db import models
class product(models.Model):
    productname=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    rating=models.CharField(max_length=30)
    catagory=models.CharField(max_length=30)
