from rest_framework import serializers
from api.models import API,UserSelectedAPI

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = '__all__'


class APISelectionSerializer(serializers.Serializer):
    selected_apis = serializers.ListField(child=serializers.IntegerField())

    
class SelectAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSelectedAPI
        fields = '__all__'

class UserSelectedAPISerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    api_names = serializers.SerializerMethodField()
    endpoints = serializers.SerializerMethodField()
    # api_name = serializers.ReadOnlyField(source='apis.name')

    class Meta:
        model = UserSelectedAPI
        fields = ['user', 'user_name', 'api_names', 'endpoints']

    def get_api_names(self, obj):
        return [api.name for api in obj.api.all()]

    def get_endpoints(self, obj):
        return [api.endpoint for api in obj.api.all()]