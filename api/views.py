

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics

from api.models import CustomAPI,UserSelectedAPI
from api.serializer import CustomAPISerializer,UserSelectedAPISerializer
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response



class APIViewSet(viewsets.ModelViewSet):
    queryset = CustomAPI.objects.all()
    serializer_class = CustomAPISerializer
    http_method_names = ['get']  # Only allow the GET method for listing

    @swagger_auto_schema()
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    


    
class UserSelectedAPIView(generics.CreateAPIView):
    serializer_class = UserSelectedAPISerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .utils import get_user_api_list

from django.urls import path
from django.utils.module_loading import import_string
from drf_yasg.views import get_schema_view as get_swagger_view
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg import renderers


def generate_dynamic_urls(api_list):
    api_patterns = []

    for api_data in api_list:
        api_id = api_data['api']
        try:
            api = CustomAPI.objects.get(id=api_id)
            # print(api)
            view_class = import_string(api.view_class)
            api_pattern = {
                'path': api.path,
                'view_class': view_class.as_view(),
                # 'view_class_name': view_class.__name__,
                'name': api.name
            }
            api_patterns.append(api_pattern)
        except CustomAPI.DoesNotExist:
            print(f"API with ID {api_id} does not exist")

    return api_patterns



# schema_view = get_swagger_view(
#     openapi.Info(
#         title="API Documentation",
#         default_version='v1',
#     ),
#     public=False,
#     permission_classes=[IsAuthenticated],
    

# )


# class MyView(APIView):
    
#     def get(self, request, *args, **kwargs):
#         user = request.user
#         api_list = get_user_api_list(user)
#         api_patterns = generate_dynamic_urls(api_list)
#         print(api_patterns)
#         serializer = CustomAPISerializer(api_list, many=True)
#         schema_view.patterns = api_patterns
#         schema = schema_view.get_schema(request=request)
#         # return Response(schema)
#         return Response(schema_view.with_ui(request, renderer='swagger'))
import json

class MyView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        api_list = get_user_api_list(user)
        api_patterns = generate_dynamic_urls(api_list)
        print(api_patterns)
        # serializer = CustomAPISerializer(api_list, many=True)
        

        return JsonResponse(json.dumps(api_patterns), safe=False)

