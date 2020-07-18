#https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
#https://blog.usejournal.com/serving-react-and-django-together-2089645046e4
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero


def index(request):
    return render(request, "build/index.html")
    
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
# Create your views here.
