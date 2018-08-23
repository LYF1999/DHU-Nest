from rest_framework.permissions import BasePermission


class ProfilePermission(BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_superuser
        return True

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        return request.user == obj.user or request.user.is_superuser
