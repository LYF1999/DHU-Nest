from rest_framework import serializers
from .models import Post
from profile.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

    author = UserSerializer(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data, author=self.context['request'].user)
