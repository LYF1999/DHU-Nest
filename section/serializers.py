from rest_framework import serializers
from .models import Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['name']

    def create(self, validated_data):
        return Section.objects.create(name=validated_data['name'], creator=self.context['request'].user)
