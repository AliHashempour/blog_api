from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrAdminElseReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff
