from .models import location
from rest_framework import serializers


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = location
        fields = ('bus_id', 'phone_id', 'latitude', 'longitude')
