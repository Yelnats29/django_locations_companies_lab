from django.shortcuts import render
from rest_framework import generics
from .serializers import CompaniesSerializer
from .models import Companies

# Create your views here.

# /coompanies POST, GET
class CompaniesList(generics.ListCreateAPIView):
    queryset = Companies.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = CompaniesSerializer # tell django what serializer to use

# /companies/:id
class CompaniesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Companies.objects.all().order_by('id')
    serializer_class = CompaniesSerializer