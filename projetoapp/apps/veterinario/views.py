from django.shortcuts import render
from .models import Veterinario
from rest_framework import viewsets
from .serializer import VeterinarioSerializer

# Create your views here.

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer  