from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Posts, Details, Info, Prescriptions, Tests
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password']


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'name' , 'content']


class DetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = ['uid', 'gender' , 'qrcode' , 'bloodgroup']


class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Info
        fields = ['uid', 'bp' , 'illness1', 'vaccination1', 'vaccination2' , 'bloodsugarlevel']


class PrescriptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prescriptions
        fields = ['uid', 'd' , 'medicine' , 'qty' , 'interval']


class TestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tests
        fields = ['uid', 'd' , 'tname', 'pdf']



