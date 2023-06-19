from rest_framework import serializers
from face_name_match.models import Facematching, StringMatching

class FaceMatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facematching
        # fields='__all__'
        exclude=(
            "created_on",
            "updated_on",
            "is_deleted",
            "match_percentage",
            "message"
            )

class StringMatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model=StringMatching
        exclude=(
            "created_on",
            "updated_on",
            "is_deleted",
            "match_percentage"
            )
