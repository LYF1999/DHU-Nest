from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from .services import ProfileService


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'desc', 'avatar']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'desc', 'avatar']

    desc = serializers.SerializerMethodField(read_only=True)
    avatar = serializers.SerializerMethodField(read_only=True)

    def get_desc(self, obj):
        profile = ProfileService.get_profile_by_user(obj)
        return profile and profile.desc

    def get_avatar(self, obj):
        profile = ProfileService.get_profile_by_user(obj)
        return profile and profile.avatar


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'email']

    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data['email'])
        profile = Profile.objects.create(user=user)
        return profile
