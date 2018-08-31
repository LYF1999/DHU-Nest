from rest_framework import serializers
from .models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['owner', 'abstract', 'thumb', 'context']


class GetCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'owner', 'abstract', 'thumb', 'context']


class CollectionIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id']
