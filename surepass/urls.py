from django.contrib import admin
from django.urls import path
from surepass.views import AadhaarVerificationView, OtpVerificationView, PanVerificationView

urlpatterns = [
    
    path('PanVerification/', PanVerificationView.as_view()),
    path('AadhaarVerification/', AadhaarVerificationView.as_view()),
    path('AadhaarVerifiedData/', OtpVerificationView.as_view()),
    

]
