from django.db import models
from utils.models import TimeStampedModel
from jsonfield import JSONField
from django.conf import settings

class PanAPI(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    pan_number = models.CharField(max_length=10)
    response_data = JSONField(null=True)


class AadhaarAPI(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    aadhaar_number = models.BigIntegerField(max_length=12)
    response_data = JSONField(null=True)

class OtpVerificationAPI(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    client_id = models.CharField(max_length=200)
    otp = models.IntegerField(max_length=6)
    response_data = JSONField(null=True)