from rest_framework import serializers
from profile.serializers import UserSerializer
from django.contrib.auth.models import User
from .models import Post
from .services import PostService
import uuid
import datetime


class PostSerializer(serializers.Serializer):
    author = serializers.SerializerMethodField(read_only=True)
    id = serializers.CharField(read_only=True)
    content = serializers.CharField()
    title = serializers.CharField()
    created_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only=True)
    active_time = serializers.DateTimeField(read_only=True)

    def get_author(self, obj: Post):
        return UserSerializer(User.objects.get(id=obj.author)).data

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user.id
        validated_data['id'] = str(uuid.uuid1())
        time = datetime.datetime.now()
        validated_data['created_time'] = time
        validated_data['updated_time'] = time
        validated_data['active_time'] = time

        return PostService.save(Post(**validated_data))

    def update(self, instance: Post, validated_data):
        validated_data['author'] = instance.author
        validated_data['id'] = instance.id
        validated_data['created_time'] = instance.created_time
        time = datetime.datetime.now()
        validated_data['updated_time'] = time
        validated_data['active_time'] = time

        return PostService.update(Post(**validated_data))
