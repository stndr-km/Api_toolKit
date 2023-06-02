from django.db import models

from utils.models import TimeStampedModel
# Create your models here.

class DedueCheck(TimeStampedModel):
    user=models.CharField(max_length=200,null =True)
    pan=models.charField(max_length=10,null=True)