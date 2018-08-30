from rest_framework import serializers
from .models import Collection
from profile.serializers import UserSerializer


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        module = Collection
        field = ['abstract', 'thumb', 'context']

    owner = UserSerializer(read_only=True)

    def create(self, validated_data):
        return Collection.objects.create(**validated_data, owner=self.context['request'].user)
