from django.db import models

class Food_details(models.Model):
    Hotelname=models.CharField(max_length=30)
    Rating=models.CharField(max_length=30)
    Item=models.CharField(max_length=30)
    Price=models.CharField(max_length=10)
    Contact=models.CharField(max_length=10)
    Address=models.CharField(max_length=30)