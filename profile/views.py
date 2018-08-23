from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from profile.models import Profile
from profile.permissions import ProfilePermission
from profile.serializers import ProfileSerializer, CreateUserSerializer


class ProfileViewSets(ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = (ProfilePermission, permissions.IsAuthenticated)
    serializer_class = ProfileSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return ProfileSerializer


