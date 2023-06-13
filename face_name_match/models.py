from django.db import models
from utils.models import TimeStampedModel
# Create your models here.

class Facematching(TimeStampedModel):
    user=models.CharField(max_length=200,null =True)
    match_percentage=models.FloatField(null=True)
    image1 = models.ImageField(upload_to='facematch/')
    image2 = models.ImageField(upload_to='facematch/')
    message=models.CharField(max_length=200, null=True) 

class StringMatching(TimeStampedModel):
    name1=models.CharField(max_length=200,null=True)
    name2=models.CharField(max_length=200,null=True)
    match_percentage=models.FloatField(null=True)