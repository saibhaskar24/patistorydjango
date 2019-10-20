from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, PostsSerializer , DetailsSerializer, InfoSerializer, PrescriptionsSerializer, TestsSerializer
from .models import Posts


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class DetailsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = DetailsSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class InfoViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = InfoSerializer

class PrescriptionsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PrescriptionsSerializer


class TestsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = TestsSerializer

