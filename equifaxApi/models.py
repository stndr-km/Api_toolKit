from django.db import models
from utils.models import TimeStampedModel
# Create your models here.

class EquifaxAPI(TimeStampedModel):
    FirstName=models.CharField(max_length=200, null=True)
    PanNumber=models.CharField(max_length=10,null=True)
    DOB=models.DateField(null=True)
    AddressLine1=models.CharField(max_length=200,null=True)
    State=models.CharField(max_length=100,null=True)
    Postal=models.IntegerField(null=True)

    response_data = models.JSONField()