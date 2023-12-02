from django.shortcuts import render
from .models import Tutor
from rest_framework import viewsets
from .serializer import TutorSerializer

# Create your views here.

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer  