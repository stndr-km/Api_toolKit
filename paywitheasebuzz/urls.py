from django.urls import re_path
from paywitheasebuzz import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^initiate_payment/$', views.initiate_payment, name="initiate_payment"),
    re_path(r'^transaction/$', views.transaction, name="transaction"),
    re_path(r'^transaction_date/$', views.transaction_date, name="transaction_date"),
    re_path(r'^refund/$', views.refund, name="refund"),
    re_path(r'^payout/$', views.payout, name="payout"),
    re_path(r'^response/$', csrf_exempt(views.response), name="response"),
]

urlpatterns += staticfiles_urlpatterns()
