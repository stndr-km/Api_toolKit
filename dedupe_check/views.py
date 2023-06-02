from django.shortcuts import render
from dedupe_check.models import DedueCheck
from dedupe_check.serializer import DedueCheckSerializer
from rest_framework import generics,status
from utils.restful_response import send_response

# Create your views here.

class DedueCheckView(generics.CreateAPIView):

    queryset=DedueCheck.objects.all()
    serializer_class=DedueCheckSerializer

    def post(self,request ,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        deduecheck=DedueCheck()
        user=request.data.get("user")
        pan=request.data.get("pan")
        deduecheck.user=user
        deduecheck.pan=pan
        deduecheck.save()

        return send_response(
                    status=status.HTTP_201_CREATED,
                    ui_message='Created',
                    developer_message="done"
                )
        
