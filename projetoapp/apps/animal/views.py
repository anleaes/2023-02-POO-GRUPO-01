from django.shortcuts import render
from .models import Animal
from rest_framework import viewsets
from .serializer import AnimalSerializer

# Create your views here.

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer  