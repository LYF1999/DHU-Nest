from rest_framework import permissions


class ForbidUpdate(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.method == 'DELETE':
            return True
        return False


def get_only_owner_can_write(field):
    class OnlyOwnCanWrite(permissions.BasePermission):
        def has_permission(self, request, view):
            return True

        def has_object_permission(self, request, view, obj):
            if request.method not in permissions.SAFE_METHODS:
                return getattr(obj, field) == request.user
            return True

    return OnlyOwnCanWrite
