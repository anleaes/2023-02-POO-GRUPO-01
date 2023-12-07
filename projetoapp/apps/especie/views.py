from django.shortcuts import render
from .models import Especie
from rest_framework import viewsets
from .serializer import EspecieSerializer

# Create your views here.

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer  