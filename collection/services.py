from .models import Collection


class CollectionServices:

    @classmethod
    def get_collection_list_by_user(cls, user):
        try:
            collections_list = Collection.objects.filter(owner=user)
            return collections_list
        except:
            return None
