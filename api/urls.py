from django.urls import include, path
from api.views import APIViewSet,UserSelectedAPIListView,UserSelectedAPIListAPIView,UserSelectedAPIView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as get_swagger_view
    # from api.swagger import get_swagger_view_with_selected_apis, get_selected_apis
from .swagger import get_swagger_view_with_selected_apis
from rest_framework import permissions
from EquifaxAPI.views import EquifaxAPI
from face_name_match.views import FacematchingView,StringMatchingView

# router = routers.DefaultRouter()
# router.register('api', APIViewSet)

# # Define the Swagger/OpenAPI schema view

schema_view = get_swagger_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[path('api-list/', APIViewSet.as_view({'get': 'list'}), name='api-list'),
              path('api-selection/', UserSelectedAPIListView.as_view(), name='api-selection'),
    path('api/user-selected-apis/', UserSelectedAPIListAPIView.as_view(), name='user-selected-apis'),
    path('bureauscore/', EquifaxAPI.as_view()),
    path('facematching/', FacematchingView.as_view(), name="Facematching-API"),
    path('namematching/', StringMatchingView.as_view(), name="Name_Matching-API"),
    ],
)


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path('api-list/', APIViewSet.as_view({'get': 'list'}), name='api-list'),
    # path('api/', include(router.urls)),
    path('api-selection/', UserSelectedAPIListView.as_view(), name='api-selection'),
    path('api/user-selected-apis/', UserSelectedAPIListAPIView.as_view(), name='user-selected-apis'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path('swagger/', get_swagger_view_with_selected_apis),
    # path('swagger/', get_swagger_view_with_selected_apis, name='schema-swagger-ui'),
    # path('swagger/<str:format>/', get_swagger_view_with_selected_apis, name='swagger-ui'),
]
    

  



    

