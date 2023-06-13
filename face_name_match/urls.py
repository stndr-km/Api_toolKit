from django.contrib import admin
from django.urls import path
from face_name_match.views import FacematchingView,StringMatchingView

urlpatterns = [
    path('facematching/', FacematchingView.as_view(), name="Facematching-API"),
    path('namematching/', StringMatchingView.as_view(), name="Name_Matching-API"),
]
