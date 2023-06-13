


from django.contrib import admin
from django.urls import path
from EquifaxAPI.views import EquifaxAPI

urlpatterns = [
    
    path('bureauscore/', EquifaxAPI.as_view())

]
