from django.shortcuts import render
from .models import Ong
from rest_framework import viewsets
from .serializer import OngSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer  
