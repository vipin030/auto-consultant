from django.contrib.auth.models import User, Group
from rest_framework import serializers

from myapp.models import *


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class VehicleSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    #user = UserSerializer()
    class Meta:
        model = Vehicle
        fields = ['name', 'type', 'buying_price', 'purchase_date', 'user']

class VehicleSoldSerializer(serializers.ModelSerializer):

    vehicle = serializers.SlugRelatedField(queryset=Vehicle.objects.all(), slug_field='name')
    #vehicle = serializers.StringRelatedField()
    class Meta:
        model = VehicleSold
        fields = ['vehicle', 'price', 'selling_date', 'seller', 'buyer', 'updated_date']
        ookup_field = 'vehicle'
