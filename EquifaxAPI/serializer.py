
from rest_framework import serializers
from EquifaxAPI.models import EquifaxAPI

class EquifaxResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquifaxAPI
        fields = '__all__'
