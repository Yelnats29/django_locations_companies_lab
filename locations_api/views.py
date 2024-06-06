from django.shortcuts import render
from rest_framework import generics
from .serializers import LocationsSerializer
from .models import Locations

# Create your views here.

# /coompanies POST, GET
class LocationsList(generics.ListCreateAPIView):
    queryset = Locations.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = LocationsSerializer # tell django what serializer to use

# /companies/:id
class LocationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locations.objects.all().order_by('id')
    serializer_class = LocationsSerializer