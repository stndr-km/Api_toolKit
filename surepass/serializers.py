from rest_framework import serializers
from surepass.models import AadhaarAPI, OtpVerificationAPI, PanAPI
class PanResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanAPI
        exclude=(
            "created_on",
            "updated_on",
            "is_deleted",
            "response_data"    
        )

class AadhaarResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AadhaarAPI
        exclude=(
            "created_on",
            "updated_on",
            "is_deleted",
            "response_data"    
        )

class OtpResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpVerificationAPI
        exclude=(
            "created_on",
            "updated_on",
            "is_deleted",
            "response_data"    
        )