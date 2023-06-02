from rest_framework import serializers
from api.models import Facematching, StringMatching

class FaceMatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facematching
        fields='__all__'

class StringMatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model=StringMatching
        fields='__all__'
