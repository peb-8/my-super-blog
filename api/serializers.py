from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Journey, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = ['id', 'name']
