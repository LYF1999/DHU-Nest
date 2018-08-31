from rest_framework import serializers
from .models import Collection
from collection.services import CollectionServices


class CollectionsListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        collections = [Collection(**item) for item in validated_data]
        return Collection.objects.bulk_create(collections)


class CollectionSerializer(serializers.ModelSerializer):
    abstract = serializers.SerializerMethodField(read_only=True)
    thumb = serializers.SerializerMethodField(read_only=True)
    context = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Collection
        list_serializer_class = CollectionsListSerializer
        fields = ['abstract', 'thumb', 'context']

    def get_abstract(self, obj):
        collections = CollectionServices.get_collection_list_by_user(obj)
        return collections and [collection.abstract for collection in collections]

    def get_thumb(self, obj):
        collections = CollectionServices.get_collection_list_by_user(obj)
        return collections and [collection.thumb for collection in collections]

    def get_context(self, obj):
        collections = CollectionServices.get_collection_list_by_user(obj)
        return collections and [collection.context for collection in collections]


class CreateCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['owner', 'abstract', 'thumb', 'context']
