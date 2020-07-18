#https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
# Create your views here.
