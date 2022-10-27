from rest_framework import permissions


class OwnAccountPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and obj.id == request.user.id)


class OnlyAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_superuser)