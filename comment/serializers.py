from rest_framework import serializers
from .models import Comment
from profile.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'reply']

    author = UserSerializer(read_only=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data,
                                      author=self.context['request'].user)
