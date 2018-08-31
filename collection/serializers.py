from rest_framework import serializers
from .models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['owner', 'abstract', 'thumb', 'context']
