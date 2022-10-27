from rest_framework import permissions


class AuthSellerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        return bool(request.user.is_authenticated and request.user.is_seller)


class OwnProductSellerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True

        return bool(request.user.is_authenticated and request.user.id == obj.seller.id)