from django.shortcuts import render

# from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import generics
from .models import Pet
from .serializer import PetSerializer

class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer 

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer