from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from utils.permissions import get_only_owner_can_write, ForbidUpdate


class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, get_only_owner_can_write('author'), ForbidUpdate]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['post']

# Create your views here.
