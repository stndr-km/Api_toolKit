from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class API(models.Model):
    name = models.CharField(max_length=100)
    endpoint = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserSelectedAPI(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    api = models.ManyToManyField(API,related_name='selected_apis')  

    def __str__(self):
        return f"User: {self.user}, APIs: {self.api.count()}"

    
    # def __str__(self):
    #     return str(self.user)