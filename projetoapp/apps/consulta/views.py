from django.shortcuts import render
from .models import Consulta
from rest_framework import viewsets
from .serializer import ConsultaSerializer

# Create your views here.

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer  