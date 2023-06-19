from rest_framework import generics

from . import models
from . import serializers
from users.models import CustomUser
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password


class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


def LoginPage(request):
    if request.method=='POST':
        userlogin=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(userlogin,pass1) 
        try:
            # Check if a user with the given username and password exists
            
            user = CustomUser.objects.get(username=userlogin)
            
            if check_password(pass1, user.password):
                print(user)

            # login(request,user)
            return redirect('list/')
        except CustomUser.DoesNotExist:
            # User does not exist or credentials are incorrect
            return HttpResponse("Username or password is incorrect")

        

    return render(request,'login.html')