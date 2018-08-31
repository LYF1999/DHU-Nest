from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response, status
from rest_framework.decorators import action
from collection.models import Collection
from collection.serializers import CollectionSerializer
from utils.permissions import get_only_owner_can_write
from collection.services import CollectionServices


class CollectionViewSets(ModelViewSet):
    queryset = Collection.objects.all()
    permission_classes = [permissions.IsAuthenticated, get_only_owner_can_write('owner')]
    serializer_class = CollectionSerializer

    @action(detail=False, permission_classes=(permissions.IsAuthenticated,))
    def my_collections(self, request):
        queryset = CollectionServices.get_collection_list_by_user(request.user)
        serializer = CollectionSerializer(queryset,many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)