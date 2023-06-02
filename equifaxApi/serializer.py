from rest_framework import serializers
from equifaxApi.models import EquifaxAPI

class EquifaxResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquifaxAPI
        fields = '__all__'
