from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from utils.permissions import get_only_owner_can_write
from utils.decorators import with_es_exceptions
from .services import PostService


class PostViewSets(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, get_only_owner_can_write('author')]
    serializer_class = PostSerializer

    def get_queryset(self):
        return PostService.find_posts_by_user_id(self.request.user.id)

    @with_es_exceptions
    def get_object(self):
        return PostService.get_by_id(id=self.kwargs['pk'])

    def destroy(self, request, *args, **kwargs):
        return PostService.delete_by_id(self.kwargs['pk'])
