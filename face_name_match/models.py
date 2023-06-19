from django.db import models
from utils.models import TimeStampedModel
# Create your models here.
from django.conf import settings

class Facematching(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    match_percentage=models.FloatField(null=True)
    image1 = models.ImageField(upload_to='facematch/')
    image2 = models.ImageField(upload_to='facematch/')
    message=models.CharField(max_length=200, null=True) 

class StringMatching(TimeStampedModel): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name1=models.CharField(max_length=200,null=True) 
    name2=models.CharField(max_length=200,null=True)
    match_percentage=models.FloatField(null=True)