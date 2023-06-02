from django.contrib import admin
from django.urls import path
from dedupe_check.views import check_customer_exists


urlpatterns = [
   # path('dedue_check', DedueCheckView.as_view(),name='dedueCheck'),
   path('check-customer/', check_customer_exists, name='check_customer'),
]
