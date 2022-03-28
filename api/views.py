from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from api.models import Journey, Post

from .serializers import UserSerializer, JourneySerializer, PostSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class JourneyViewSet(ModelViewSet):

    queryset = Journey.objects.all()
    serializer_class = JourneySerializer


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
