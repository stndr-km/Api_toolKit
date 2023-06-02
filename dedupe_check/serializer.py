from rest_framework import serializers
from dedupe_check.models import DedueCheck

class DedueCheckSerializer:
    class meta:
        model=DedueCheck
        fields='__all__'
