from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from utils.permissions import get_only_owner_can_write


class PostViewSets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated, get_only_owner_can_write('author')]
    serializer_class = PostSerializer
# Create your views here.
