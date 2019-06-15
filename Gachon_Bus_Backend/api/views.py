from django.shortcuts import render

#API
from rest_framework import viewsets
from .serializers import LocationSerializer
from .models import location
#END

class LocationViewSet(viewsets.ModelViewSet):
    queryset = location.objects.all()
    serializer_class = LocationSerializer