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
                owner = getattr(obj, field)
                if type(owner) == int:
                    return owner == request.user.id

                return owner == request.user
            return True

    return OnlyOwnCanWrite
