from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from .models import UserSelectedAPI
from django.utils.module_loading import import_string
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

from django.urls import path


from .models import UserSelectedAPI

def get_user_api_list(user):
    try:
        user_selected_api = UserSelectedAPI.objects.filter(user=user)
        api_list = list(user_selected_api.values('api'))
        return api_list
    except UserSelectedAPI.DoesNotExist:
        return []

   
# class MyView(APIView):
#     def get(self, request, *args, **kwargs):
#         api_patterns = get_user_api_list(request.user)
#         return Response(api_patterns)

