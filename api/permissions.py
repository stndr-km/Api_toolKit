from rest_framework.permissions import BasePermission
from .models import UserSelectedAPI

class UserAPIPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        api_id = view.get_object().id
        return UserSelectedAPI.objects.filter(user=user, api__id=api_id).exists()
