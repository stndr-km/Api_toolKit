from django.urls import include, path, re_path
from api.views import APIViewSet,UserSelectedAPIView,MyView,generate_dynamic_urls
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as get_swagger_view
from users.models import CustomUser


# from EquifaxAPI.views import EquifaxAPI
# from face_name_match.views import FacematchingView,StringMatchingView
from api.models import CustomAPI,UserSelectedAPI
from django.utils.module_loading import import_string
from rest_framework.permissions import IsAuthenticated
from .utils import get_user_api_list
from rest_framework.response import Response
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

from rest_framework.views import APIView
from django.shortcuts import redirect
from django.urls.resolvers import URLPattern
import json
from django.http import JsonResponse,HttpResponse


x =[]



def generate_dynamic():
    patterns=x
    print(x,"dynmic funct")
    print(patterns)
    api_patterns = []
    for api_data in patterns: 

        path_value = api_data['path']
        # print(path_value,"path")
        view_class = api_data['view_class'].__name__
        print(type(view_class),view_class,"view_class")
        # name_value = api_data['name']
        converted_pattern = f"path('{path_value}', {view_class}.as_view(), name='{api_data['name']}')"
        api_patterns.append(converted_pattern)
        # api_patterns.append(path(path_value, view_class, name=name_value))
        
        print(converted_pattern)
    for path_string in api_patterns:
        print('hjsgfhjjkbjkh')
        path_object = eval(path_string)
        # api_patterns.append(path_object)
        urlpatterns.append(path_object)

    print("patterns",type(api_patterns),api_patterns)
    return path_object


class MyView(APIView):
    
    def get(self, request, *args, **kwargs):
        user = request.user
        api_list = get_user_api_list(user)
        x.append( generate_dynamic_urls(api_list)[0])
        patterns=generate_dynamic_urls(api_list)
        print(x,"myview X")
        print(patterns,"myview patter")
        # print(api_patterns)
        
        generate_dynamic()
        converted_data = [] 

        for item in patterns:
            # print(item)
            path = item['path']
            # print(path)
            view_class = item['view_class'].__name__
            name = item['name']
            converted_data.append(f"path('{path}', {view_class}.as_view(), name='{name}')")
        # print(converted_data)
        

        # x.append(converted_data[0])
        return Response()
    
schema_view = get_schema_view(
      openapi.Info(
         title="Snippets API",
         default_version='v1',
         description="Test description",
         terms_of_service="https://www.google.com/policies/terms/",
         contact=openapi.Contact(email="contact@snippets.local"),
         license=openapi.License(name="BSD License"),
      ),
      public=True,
      permission_classes=(permissions.AllowAny,),
      
      
)
        


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    

    path('api-list/', APIViewSet.as_view({'get': 'list'}), name='api-list'),
    # path('api/', include(router.urls)),
    path('api-selection/', UserSelectedAPIView.as_view(), name='api-selection'),
    # path('api/user-selected-apis/', UserSelectedAPIListView.as_view(), name='user-selected-apis'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('test/',MyView.as_view(), name='api_list'),
    # path('dynac/', include(generate_dynamic())), 
    
]
