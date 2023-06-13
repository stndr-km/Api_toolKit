from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import generics
from .models import UserSelectedAPI,API
from api.serializer import APISerializer,UserSelectedAPISerializer,APISelectionSerializer,SelectAPISerializer
from rest_framework.response import Response
from rest_framework import status



class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)

        # Get the user-selected APIs for the current user
        user_selected_apis = UserSelectedAPI.objects.filter(user=request.user).prefetch_related('api')

        # Collect the unique API IDs for the user-selected APIs
        api_ids = []
        for user_selected_api in user_selected_apis:
            api_ids.extend(user_selected_api.api.values_list('id', flat=True))

        # Filter the paths and operations based on the user-selected APIs
        paths = schema.paths.copy()
        for path, path_item in schema.paths.items():
            operations = path_item.copy()
            for method, operation in path_item.items():
                if operation.operation_id not in api_ids:
                    del operations[method]
            if not operations:
                del paths[path]
            else:
                paths[path] = operations

        schema.paths = paths
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API documentation",
    ),
    public=True,
    generator_class=CustomSchemaGenerator,
)


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


def get_swagger_view_with_selected_apis(request):
    user_selected_apis = UserSelectedAPI.objects.filter(user=request.user).select_related('api')
    api_ids = [str(api.api.id) for api in user_selected_apis]

    # Pass the selected API IDs as a query parameter to the Swagger UI
    extra_query_params = {'selected_apis': ','.join(api_ids)}

    return schema_view.with_ui('swagger', cache_timeout=0, query_params=extra_query_params)(request)
