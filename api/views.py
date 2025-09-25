from django.shortcuts import render
from .models import Alimento, RegistroComida
from .serializers import AlimentoSerializer, RegistroComidaSerializer
from rest_framework import viewsets
# Create your views here.

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer

class RegistroComidaViewSet(viewsets.ModelViewSet):
    queryset = RegistroComida.objects.all()
    serializer_class = RegistroComidaSerializer
