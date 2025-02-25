from rest_framework import permissions

from django.contrib.auth import get_user_model

User = get_user_model()


class IsAdminOrReadOnly(permissions.BasePermission):

    # code = ''
    # message = ''

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user.is_superuser
        )


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user == obj.author or
            request.user.is_superuser
        )


class IsSalesmanOrReadOnly(permissions.BasePermission):
    message = 'Пользователь должен быть продавцом.'

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user.role == User.SALESMAN or
            request.user.is_superuser
        )


class IsSalesman(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user.role == User.SALESMAN or
            request.user.is_superuser
        )


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user == obj.author or
            request.user.is_superuser
        )