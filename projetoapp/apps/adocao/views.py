from django.shortcuts import render
from .models import Adocao
from rest_framework import viewsets
from .serializer import AdocaoSerializer

# Create your views here.

class AdocaoViewSet(viewsets.ModelViewSet):
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer  