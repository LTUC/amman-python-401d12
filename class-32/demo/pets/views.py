from django.shortcuts import render

# from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import generics
from .models import Pet
from .serializer import PetSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer 
    permission_classes = [IsAuthenticated]

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsOwnerOrReadOnly]
