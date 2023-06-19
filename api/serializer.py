from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.models import CustomAPI, UserSelectedAPI
from users.models import CustomUser
from django.contrib.auth.models import User


class CustomAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAPI
        fields = '__all__'



class UserSelectedAPISerializer(serializers.ModelSerializer):   
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    api = serializers.PrimaryKeyRelatedField(
        queryset=CustomAPI.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = UserSelectedAPI
        fields = ['user', 'api']

    def create(self, validated_data):
        api_data = validated_data.pop('api')
        user_selected_api = UserSelectedAPI.objects.create(**validated_data)
        for api in api_data:
            user_selected_api.api.add(api)
        return user_selected_api

