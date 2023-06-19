
from rest_framework import serializers
from EquifaxAPI.models import EquifaxAPI
class EquifaxResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquifaxAPI
        exclude=(
            "created_on",
            "updated_on",
            "is_deleted",
            "response_data"
            
        )
    
