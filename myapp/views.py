from django.contrib.auth.models import User, Group
from rest_framework import viewsets
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend

#from django_filters.rest_framework import FilterSet, filters
from myapp.serializers import UserSerializer, GroupSerializer, VehicleSerializer, VehicleSoldSerializer
from myapp.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined').prefetch_related('groups')
    serializer_class = UserSerializer
    filter_backend = [DjangoFilterBackend]
    filter_fields = ['username', 'email']


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BorrowedFilterSet(django_filters.FilterSet):
   missing = django_filters.BooleanFilter(field_name='returned', lookup_expr='isnull')

   class Meta:
       model = Vehicle
       fields = ['name']


class VehicleViewSet(viewsets.ModelViewSet):

    queryset = Vehicle.objects.all().select_related('user')
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'type']


class VehicleSoldViewSet(viewsets.ModelViewSet):

    queryset = VehicleSold.objects.all()
    serializer_class = VehicleSoldSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['selling_date']
