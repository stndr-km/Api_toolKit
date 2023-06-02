from django.db import models
from utils.models import TimeStampedModel
# Create your models here.

class EquifaxAPI(TimeStampedModel):
    customer_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    response_data = models.JSONField()