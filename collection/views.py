from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response, status
from rest_framework.decorators import action
from collection.models import Collection
from collection.serializers import CollectionSerializer, GetCollectionSerializer, CollectionIdSerializer
from utils.permissions import get_only_owner_can_write
from collection.services import CollectionServices
from django.http import JsonResponse
from django.views.decorators.http import require_POST


class CollectionViewSets(ModelViewSet):
    queryset = Collection.objects.all()
    permission_classes = (permissions.IsAuthenticated, get_only_owner_can_write('owner'))
    serializer_class = CollectionSerializer

    @action(detail=False, permission_classes=(permissions.IsAuthenticated,))
    def my_collections(self, request):
        queryset = CollectionServices.get_collection_list_by_user(request.user)
        serializer = GetCollectionSerializer(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, permission_classes=(permissions.IsAuthenticated,))
    def delete_collection(self, request):
        if request.method == 'GET':
            return response.Response(status=status.HTTP_200_OK)
        elif request.method == 'POST':
            queryset = CollectionServices.get_owners_collection_by_id(request.user, request.data['id'])
            if len(queryset) == 1:
                queryset.delete()
                return JsonResponse({'msg': 'Collection_deleted_ok'}, status=status.HTTP_200_OK)
            else:
                return response.Response(status=status.HTTP_404_NOT_FOUND)
