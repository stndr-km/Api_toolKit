from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',Sign)
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('equifax/',include('EquifaxAPI.urls')),
    path('face_name_match/',include('face_name_match.urls')),
    path('users/', include('users.urls')),
    path('paywitheasebuzz/',include('paywitheasebuzz.urls')),
    path('surepass/',include('surepass.urls')),
]
