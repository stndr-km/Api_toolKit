from django.urls import include, path

from . import views

urlpatterns = [
    path('list/', views.UserListView.as_view()),
    path('', views.LoginPage,name='Login')
]
