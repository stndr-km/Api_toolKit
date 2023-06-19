from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class CustomAPI(models.Model):
    path = models.CharField(max_length=100)
    view_class = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserSelectedAPI(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    api = models.ManyToManyField(CustomAPI, related_name='selected_apis')

    def __str__(self):
        return f"User: {self.user}, APIs: {self.api.count()}"


class UserUrlpatternList:
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)