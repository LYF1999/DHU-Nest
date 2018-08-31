from .models import Collection
from django.core.exceptions import ObjectDoesNotExist


class CollectionServices:

    @classmethod
    def get_collection_list_by_user(cls, user):
        try:
            collections_list = Collection.objects.filter(owner=user).order_by('id')
            return collections_list
        except ObjectDoesNotExist:
            return None

    @classmethod
    def get_owners_collection_by_id(cls, user, id):
        try:
            collection = Collection.objects.filter(id=id).filter(owner=user)
            return collection
        except ObjectDoesNotExist:
            return None
