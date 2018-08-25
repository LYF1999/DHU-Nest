from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response, status
from rest_framework.decorators import action
from profile.models import Profile
from profile.permissions import ProfilePermission
from profile.serializers import ProfileSerializer, CreateUserSerializer, UserSerializer


class ProfileViewSets(ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = (ProfilePermission, permissions.IsAuthenticated)
    serializer_class = ProfileSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return ProfileSerializer

    @action(detail=False, permission_classes=(permissions.IsAuthenticated,))
    def info(self, request):
        return response.Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)


