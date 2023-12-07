from django.shortcuts import render
from .models import Raca
from rest_framework import viewsets
from .serializer import RacaSerializer

# Create your views here.

class RacaViewSet(viewsets.ModelViewSet):
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer  