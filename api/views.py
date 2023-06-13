from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics

from api.models import API,UserSelectedAPI
from api.serializer import APISerializer,UserSelectedAPISerializer,APISelectionSerializer,SelectAPISerializer
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema




class APIViewSet(viewsets.ModelViewSet):
    
    queryset = API.objects.all()
    serializer_class = APISerializer
    http_method_names = ['get']  # Only allow the GET method for listing

    @swagger_auto_schema()
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserSelectedAPIView(viewsets.ModelViewSet):
    queryset = UserSelectedAPI.objects.all()
    serializer_class = UserSelectedAPISerializer
    
    

class UserSelectedAPIListAPIView(generics.ListAPIView):
    serializer_class = UserSelectedAPISerializer

    def get_queryset(self):
        user = self.request.user
        return UserSelectedAPI.objects.filter(user=user)
    

# class UserSelectedAPIListView(generics.ListCreateAPIView):
#     serializer_class = SelectAPISerializer

#     def get_queryset(self):
#         return UserSelectedAPI.objects.filter(user=self.request.user)

    

#     def perform_create(self, serializer):
#         selected_apis = self.request.data.get('selected_apis', [])
#         user = self.request.user
#         user_selected_api = UserSelectedAPI.objects.create(user=user)
#         for api_id in selected_apis:
#             api = API.objects.get(pk=api_id)
#             user_selected_api.apis.add(api)

#         serializer.save(user=user)

from rest_framework import status

class UserSelectedAPIListView(generics.ListCreateAPIView):
    serializer_class = SelectAPISerializer

    def get_queryset(self):
        return UserSelectedAPI.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['api_choices'] = API.objects.all()  # Pass all APIs as choices to the serializer
        return context

    def perform_create(self, serializer):
        selected_apis = self.request.data.get('selected_apis', [])
        user = self.request.user

        # Delete existing UserSelectedAPI instance for the user
        UserSelectedAPI.objects.filter(user=user).delete()

        # Create a new UserSelectedAPI instance and associate selected APIs
        user_selected_api = UserSelectedAPI.objects.create(user=user)
        for api_id in selected_apis:
            api = API.objects.get(pk=api_id)
            user_selected_api.apis.add(api)

        serializer.save(user=user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



