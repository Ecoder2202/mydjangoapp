from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CardSerializer
from .models import Card
class CardViewSet(viewsets.ModelViewSet):
    queryset=Card.objects.all().order_by('-id')
    serializer_class=CardSerializer
    