from django.contrib import admin
from django.urls import path
from equifaxApi.views import EquifaxAPIView

urlpatterns = [
    path('bureau_score/',EquifaxAPIView.as_view(), name='Equifax_api'),
]
